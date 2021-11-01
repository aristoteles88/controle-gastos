from django.shortcuts import render
from django.http import HttpResponse
import datetime


def home(request):
    now = datetime.datetime.now()
    # html = "<html><body>Agora são %s.</body></html>" % now
    return render(request=request, template_name="contas/home.html")
