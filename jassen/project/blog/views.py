from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.views.generic import (ListView,DetailView,CreateView,UpdateView)
from .models import Post,Category,Tags,Index 
from django.views import generic, View
# Create your views here.

class PostView(View):
    def get(self, request, post_id, *args, **kwargs):
        post = Post.objects.filter(pk=post_id).order_by('-date')
        context = {'post':post,}
        return render(request, "Post_list.html", context)
 