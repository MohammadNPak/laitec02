from django.shortcuts import render
from django.contrib import messages


def message(request):
    messages.add_message(request, messages.SUCCESS, 'test message')
    return render(request, 'message.html', {})


def index(request):

    return render(request, 'index.html', {})
