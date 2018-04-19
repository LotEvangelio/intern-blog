from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views import View, generic


from .models import Post, Index, Category, Tag
class PostView(View):

	def get(self, request, post_id, *args, **kwargs):
         post = Post.objects.filter(id=post_id)
         context = {'post':post}
         return render(request, "post_list.html", context)



class IndexView(View):

    def get(self,request,pk,*args, **kwargs):
        index = Index.objects.filter(pk=pk)
        paginator = Paginator()
        page = request.GET.get('page')
        post = paginator.get_page(page)
        context = {'index':index}
        return render(request, "index.html", {'post':post})
