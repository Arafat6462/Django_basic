from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

def post_list(request):
    posts = Post.objects.all().order_by('-pub_date') # Get all posts, ordered by publication date
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # Get a single post or return a 404 error
    comments = post.comments.all() # Get all comments related to this post
    return render(request, 'blog/detail.html', {'post': post, 'comments': comments})