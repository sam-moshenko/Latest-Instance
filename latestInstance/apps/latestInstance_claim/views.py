import random

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Node


def index(request):
    nodes = Node.objects.get_queryset().filter(parent=None)
    context = {
        'nodes': nodes
    }
    return render(request, "index.html", context)


def node(request, id):
    claim = Node.objects.get(id=id)
    nodes = Node.get_descendants(include_self=False, self=claim)

    context = {
        'claim':claim,
        'nodes':nodes
    }
    return render(request, "node.html", context)


def add(request, id):
    node = Node.objects.get(id=id)
    if request.method == 'POST':
        text = request.POST['text']
        isArgument = request.POST.get('isArgument', False)
        isArgument = True if isArgument == 'on' else False
        node = Node(text=text, argument=isArgument, parent=Node.objects.get(id=id))
        node.save()
        return redirect('/node/' + str(node.parent.id))
    else:
        context = {
            'root' : node.get_root(),
            'node' : node
        }
        return render(request, "add.html", context)

def addClaim(request):
    if request.method == 'POST':
        text = request.POST['text']
        node = Node(text=text, parent=None)
        node.save()
        return redirect('/node/' + str(node.id))
    else:
        return render(request, "addClaim.html")