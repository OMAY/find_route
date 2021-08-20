from django.shortcuts import render


def home(request):
    name = 'Django-world'
    return render(request, 'home.html', {'name': name})
