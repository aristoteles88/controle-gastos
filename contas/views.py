from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacao
from .forms import TransacaoForm
import datetime


def home(request):
    data = {}

    data['now'] = datetime.datetime.now()
    data['transacoes'] = ['t1', 't2', 't3']
    # html = "<html><body>Agora são %s.</body></html>" % now

    return render(request=request, template_name="contas/home.html", context=data)


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request=request, template_name="contas/listagem.html", context=data)


def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("url_listagem")

    data['form'] = form
    return render(request=request, template_name='contas/form.html', context=data)


def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect("url_listagem")

    data['form'] = form
    data['transacao'] = transacao
    return render(request=request, template_name='contas/form.html', context=data)


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect("url_listagem")
