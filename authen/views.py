from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from authen.form import CustomUserCreateForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreateForm()
    return render(request, 'authen/inscription.html', {'form':form})

def connexion(request):
    if request.method ==  "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username=username, password=password)
        if user is not None : 
            login (request,user)
            if (username == 'admin'  and password =='admin'):
                return redirect('/admin')
            else:
                return redirect('dashbord')
        else:
            messages.error(request, 'info incorrectes')
    return render(request,'authen/connexion.html')

@login_required
def dashbord(request):
    return render(request, 'authen/dashbord.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')