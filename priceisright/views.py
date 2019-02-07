from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    # return HttpResponse('Price is right game one')
    # this will be a simple about me page / will list website info
    return render(request, 'about.html')
