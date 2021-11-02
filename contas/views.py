from django.shortcuts import render
from django.http import HttpResponse
from .models import Transacao
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