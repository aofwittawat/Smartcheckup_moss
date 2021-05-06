from django.shortcuts import render
from checkupapp.models import UserDetail, CheckUp


def Home(request):
    return render(request, 'home.html')


def Form(request):
    if request.method == 'POST':
        print(request.POST)

    return render(request, 'checkform.html')
