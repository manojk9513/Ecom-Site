from email import message
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Register
# Create your views here.


def register(request):
    if request.method=='POST':
        form=Register(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}')
            return render('shop:home')
    else:
        form=Register()
    return render(request,'user/register.html',{'form':form})

