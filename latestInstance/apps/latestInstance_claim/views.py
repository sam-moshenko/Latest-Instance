import random

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):

    number = random.randrange(0, 100)
    context = {
        'value': 'Python',
        'number': number
    }
    return render(request, "index.html", context)
