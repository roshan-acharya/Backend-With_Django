from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#request handler and send response
def home(request):
    return HttpResponse("Hello, Django!")