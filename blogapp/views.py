from django.shortcuts import render
from .models import Post

def post_list(request):
    #posts = Post.objects.all() # posts is with queryset
    posts = Post.objects.order_by('-created_date')
    context = {"posts": posts}
    return render(request, 'blogapp/post_list.html', context)

def post_detail(request, pk):
    post_at_id = Post.objects.get(pk=pk)
    context = {'id': pk, 'post_at_id': post_at_id}
    return render(request, 'blogapp/post_detail.html', context)