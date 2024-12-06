from django.shortcuts import render

from posts.models import Post

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/postspage.html', {'posts': posts})