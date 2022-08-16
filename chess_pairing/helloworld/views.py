from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(
        request,
        template_name="helloworld/index.html"
    )

def greet(request, name:str) -> HttpResponse:
    return HttpResponse(f"hello, {name.capitalize()}")

def greet1(reqest):
    return HttpResponse("hello Georege!")

def greet2(request, name:str):
    return render(
        request,
        template_name="helloworld/greet.html",
        context={
            "name": name.capitalize()
        }
    )