from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'Authentication/homePage.html')

def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')

    context = {'form':form}
    return render(request,'Authentication/register.html',context)

def loginPage(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,email = email,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
    context={}    
    return render(request,'Authentication/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')                   
