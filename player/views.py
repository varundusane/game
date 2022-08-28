from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib import messages

from player.models import Player
from .forms import RegisterForm
from django.contrib.auth import authenticate , login

def register(request):
    form  = RegisterForm()
    # if request.method == 'GET':
    #     context = {'form': form}
    #     return render(request, 'register.html', context)
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        
        
        if form.is_valid():
            # form.save()
            
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            nickname = form.cleaned_data.get('nickname')
            password1 = form.cleaned_data.get('password1')
            user.save()
            pr = Player(user=user, nickname=nickname, password1=password1)
            pr.save()
            new_user = authenticate(username=username , password=password1)
            if new_user is not None:
                login(request, new_user)
            else: 
                form = RegisterForm()
        return render(request, 'register.html')
    else:
        print('Form is not valid')
        print(form.errors.as_data()) 
        messages.error(request, 'Error Processing Your Request')
        context = {'form': form}
    return render(request, 'register.html', context)

    return render(request, 'register.html', {})

def Dashboard(request):
    return render(request, 'dashboard.html')