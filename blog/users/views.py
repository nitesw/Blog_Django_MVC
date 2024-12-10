from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registerpage(request):
    form = UserCreationForm()
    return render(request, 'users/registerpage.html', {'form': form})