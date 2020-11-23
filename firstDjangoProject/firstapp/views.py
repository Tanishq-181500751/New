from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from firstapp.models import Students


def FirstPageController(request):
    return HttpResponse("<h1> My First Django Project</h1>")

def IndexPageController(request):
    return HttpResponse("<h1> This Is Index Page</h1>")


def HtmlPageController(request):
    return render(request,"htmlpage.html")


def HtmlPageControllerWithData(request):
    data1 = "This is data 1 passing to HTML page"
    data2 = "This is data 2 passing to HTML page"
    return render(request, "htmlpage_with_data.html", {'data': data1 , "data1": data2})


def PassingDataToController(request,url_data):
    return HttpResponse("<h2>This is data coming via URL : " +url_data)


