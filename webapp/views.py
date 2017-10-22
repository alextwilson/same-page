from django.shortcuts import render
from django.http import HttpResponse
from . import storage

def index(request):
    hello_world = '<h2>Hello world!</h2>'
    storage.Storage_Of.set_timestamp()
    local_timestamp = storage.Storage_Of.timestamp
    return HttpResponse(hello_world + str(local_timestamp))
