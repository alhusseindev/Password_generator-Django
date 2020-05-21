from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')   #note render is used instead of HttpResponse
    #it does the same thing, it returns an HttpResponse

def password(request):

    characters = list("abcdefghijklmnopqrstuvwxyz")

    if(request.GET.get("Uppercase")):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if(request.GET.get("numbers")):
        characters.extend("123456789")

    if(request.GET.get("special")):
        characters.extend(list("!@#$%^&*()_+|\?/<>;'`"))

    password_length= int(request.GET.get("length"))       #length is in home.html   casting to int to be able to edit numbers in url bar, and gives us the valid password length
    #password_length= int(request.GET.get('length', 12))  #this 12 means default password length=12
    thepassword=''

    for i in range(password_length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')