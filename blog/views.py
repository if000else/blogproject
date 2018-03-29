from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog import models
def index(request):
    post_list = models.Post.objects.all().order_by('-created_time')
    return render(request, 'blog/static/index.html', context={'post_list': post_list})
    # return render(request,'blog/static/index.html',)