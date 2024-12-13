from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registerpage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news:posts")
        else:
            print(form.errors)
    else:
        form = UserCreationForm() 

    return render(request, 'users/registerpage.html', {'form': form})
