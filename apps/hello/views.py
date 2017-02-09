from django.shortcuts import render


def home(request):
    return render(request, 'hello/home.html')
