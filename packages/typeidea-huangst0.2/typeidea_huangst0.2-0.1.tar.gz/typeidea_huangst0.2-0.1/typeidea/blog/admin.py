from django.contrib import admin
from .models import Category,Post,Tag
from django.utils.html import format_html
from django.urls import reverse
from .adminforms import PostAdminForm
from django.contrib import admin
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
from django.contrib.admin.models import LogEntry

# Register your models here.



class PostInline(admin.TabularInline): #样式不同
    fields = ('title','description')
    extra = 1 #控制额外多几个
    model = Post


@admin.register(Category,site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name','status','is_nav','created_time',)
    fields = ('name', 'status', 'is_nav',)
    inlines = [PostInline,]
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request,obj, form, change)


@admin.register(Tag,site=custom_site)
class Tagadmin(BaseOwnerAdmin):
    list_display = ('name', 'status','created_time')
    fields = ('name',"status",)
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(Tagadmin, self).save_model(request,obj, form, change)


@admin.register(Post,site=custom_site)
class Postadmin(BaseOwnerAdmin):
    class CategoryOwnerFilter(admin.SimpleListFilter):
    #自定义过滤器只展示当前用户分类
        title = "分类过滤器"
        parameter_name = "owner_category"

        def lookups(self, request, model_admin):
            return Category.objects.filter(owner=request.user).values_list('id','name')
        def queryset(self, request, queryset):
            category_id = self.value()
            if category_id:
                return queryset.filter(category_id=category_id)
            return queryset


    list_display = [
        'title', 'category', 'status',
        'created_time', 'operator','description','owner'
    ]
    list_display_links = []
    list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True
    form = PostAdminForm #使描述字段能以某种方式呈现
    #编辑动作
    save_on_top = True
    exclude = ('owner',)
    fieldsets = (
        ('基础配置',{
            'description': '基础配置描述',
            'fields':(
                ('title', 'category'),
                'status' ,
            ),
        }),
        ('内容', {
            'fields': (
                'description',
                'content',
            ),
        }),
        ('额外信息', {
            'classes': ('collapse',),
            'fields': ('tags',)
        })
    )

    def operator(self,obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(Postadmin, self).save_model(request,obj, form, change)
    def get_queryset(self, request):
        qs = super(Postadmin, self).get_queryset(request)
        return qs.filter(owner=request.user)


@admin.register(LogEntry,site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']