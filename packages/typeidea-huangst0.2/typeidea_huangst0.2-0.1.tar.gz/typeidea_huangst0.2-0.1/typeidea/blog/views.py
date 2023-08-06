from datetime import date
from django.shortcuts import render,get_object_or_404
from .models import Tag,Post,Category
from django.http import  HttpResponse
from  config.models import SideBar
from django.db.models import  Q, F
from django.views.generic import  ListView,DetailView
from django.core.cache import cache
from comment.form import CommentForm
from comment.models import Comment
# Create your views here.
class CommonViewMixin:
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars':SideBar.get_all()
        })
        context.update(Category.get_navs())
        return context

class IndexView(CommonViewMixin,ListView):
    queryset = Post.latest_posts()
    context_object_name = 'post_list'
    paginate_by = 3
    template_name = 'blog/list.html'


class CategoryView(IndexView):
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category,pk=category_id)
        context.update({
            'category': category
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)#####为什么呢

class TagView(IndexView):
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag,pk=tag_id)
        context.update({
            'tag': tag
        })
        return  context

    def get_queryset(self):
        queryset = super().get_queryset()
        tags_id = self.kwargs.get('tag_id')
        return queryset.filter(tags__id = tags_id)


class PostDetailView(CommonViewMixin,DetailView):
    queryset = Post.latest_posts()
    template_name = 'blog/detail.html'
    context_object_name = 'post' #或许一般是在父类李构造，用来传递quertset
    pk_url_kwarg = 'post_id'
    def get(self,request,*args, **kwargs):
        response = super().get(request,*args, **kwargs)
        self.handle_visited()
        return response

    def handle_visited(self):
        increase_pv = False
        increase_uv = False
        uid = self.request.uid
        pv_key = 'pv:%s:%s' %(uid,self.request.path)
        uv_key = 'uv:%s:%s:%s' %(uid,str(date.today()),self.request.path)
        if not cache.get(pv_key):
            increase_pv = True
            cache.set(pv_key,1*60)
        if not cache.get(uv_key):
            increase_uv = True
            cache.set(uv_key,24*60*60)
        if increase_pv and increase_uv:
            Post.objects.filter(pk = self.object.id).update( pv = F('pv') + 1, uv = F('uv') + 1)
        elif increase_pv:
            Post.objects.filter(pk = self.object.id).update( pv = F('pv') + 1)
        elif increase_uv:
            Post.objects.filter(pk = self.object.id).update( uv = F('uv') + 1)








class SearchView(IndexView):
    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        else:
            return queryset.filter(Q(title__icontains = keyword) | Q(description__icontains = keyword))

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        keyword = self.request.GET.get('keyword','')
        context.update({
            'keyword': keyword
        })
        return context


class AuthorView(IndexView):
    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.kwargs.get('author_id')
        return queryset.filter(owner_id = author_id)






    #获取queryset与传输context给模板的关系
    #self.kwarg.get()的数据为什么是从URL中拿到的