from django.shortcuts import redirect, render
from posts.models import Post
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/postspage.html', {'posts': posts})

@login_required(login_url='users:login')
def create_post(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  
            post.author = request.user      
            post.save()
            return redirect('news:posts')
        else:
            print(form.errors)
    else:
        form = forms.PostForm()

    return render(request, 'posts/createpostpage.html', {'form': form})