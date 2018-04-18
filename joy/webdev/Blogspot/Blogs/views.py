from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View, generic


from .models import Post, Index, Category, Tags

class PostView(View):

	template_name = "post_list.html"
	def get(self, request):
		post = Post.objects.all()
		context = {'post':post,}
		return render(request, "post_list.html", context)