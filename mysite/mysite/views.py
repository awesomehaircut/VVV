from django.http import HttpResponse
from django.shortcuts import Http404
from django.template import loader


def index(request):
    template = loader.get_template('mysite/index.html')
    context = {'hola':'adios'}
    return HttpResponse(template.render(context, request))


