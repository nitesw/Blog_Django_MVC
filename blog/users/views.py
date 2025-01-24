from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            print(form.errors)
    else:
        form = UserCreationForm() 

    return render(request, 'users/registerpage.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(f"Welcome back, {user.username}!")
            return redirect("home")
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'users/loginpage.html', {'form': form})

def logout_page(request):
    logout(request)
    print("You have been logged out.")
    return redirect("users:login")