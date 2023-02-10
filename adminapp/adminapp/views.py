from django.http import HttpResponse,request
from django.shortcuts import render


def test(request):
    # return HttpResponse('<h1>Welcome in Home page</h1>')
    return render(request,'index.html',{})