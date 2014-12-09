from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from blog.models import Blog_Post

def post(request, post_id): 
    blog_post = get_object_or_404(Blog_Post, pk=post_id)
    return render(request, 'blog/post.html', {'Blog_Post': blog_post})

def index(request): 
    latest_post_list = Blog_Post.objects.order_by('-pub_date')#[:5]
    #post_photo = Blog_Post.post_photo
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.html', context)
