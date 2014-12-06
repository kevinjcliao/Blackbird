from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from blog.models import Blog_Post

def index(request): 
    latest_post_list = Blog_Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.html', context)
