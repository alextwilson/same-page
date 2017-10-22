from django.shortcuts import render
from django.http import HttpResponse
from . import storage

def index(request):
    hello_world = '<h2>Hello world!</h2>'
    local_timestamp = storage.Storage_Of.timestamp
    return HttpResponse(hello_world + str(local_timestamp))
