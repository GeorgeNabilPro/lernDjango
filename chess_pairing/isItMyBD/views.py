from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime

def index(request):
    now = datetime.datetime.now()
    return render(
        request,
        template_name="isItMyBD/isitmybd.html",
        context={
            "birthday":now.month == 3 and now.day == 15,
        },
    )
