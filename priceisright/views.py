from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    # return HttpResponse('Price is right game one')
    return render(request, 'about.html')
