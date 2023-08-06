from django.db import models
from django.contrib.auth.models import User
import mistune
from django.utils.functional import cached_property


class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除"),
    )
    name = models.CharField(max_length=50,verbose_name="名称")
    status = models.IntegerField(choices=STATUS_ITEMS,default=STATUS_NORMAL,verbose_name="状态")
    is_nav = models.BooleanField(default=False, verbose_name="是否是导航")
    owner = models.ForeignKey(User, verbose_name="作者",on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    class Meta:
        verbose_name = verbose_name_plural = '分类'
    @classmethod
    def get_navs(cls):
        categories = Category.objects.filter(status=cls.STATUS_NORMAL)
        nav_categories = []
        normal_categories = []
        for cate in categories:
            if cate.is_nav:
                nav_categories.append(cate)
            else:
                normal_categories.append(cate)
        return {
                'navs': nav_categories,
                'categories': normal_categories
            }
    def __str__(self):
        return self.name


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除"),
    )
    name = models.CharField(max_length=10,verbose_name="名称")
    status = models.IntegerField(choices=STATUS_ITEMS,default=STATUS_NORMAL,verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    owner = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="作者")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = verbose_name_plural = '标签'


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL,"正常"),
        (STATUS_DELETE, "删除"),
        (STATUS_DRAFT,"草稿"),
    )
    title = models.CharField(max_length=255, verbose_name = "标题")
    description = models.CharField(max_length=1024, blank = True, verbose_name = "摘要")
    content = models.TextField(verbose_name="正文",help_text="正文必须为MARKDOWN格式")
    content_html = models.TextField(verbose_name="正文HTML",blank = True, editable=False)
    status = models.IntegerField(choices=STATUS_ITEMS, verbose_name="状态", default=STATUS_NORMAL)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    owner = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="作者")
    tags = models.ManyToManyField(Tag,verbose_name="标签")
    category = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name="分类")
    pv = models.PositiveIntegerField(default=1)
    uv = models.PositiveIntegerField(default=1)

    @classmethod
    def hot_post(cls,with_related = True):
        if with_related:
            return Post.objects.select_related('owner', 'category').filter(status=Post.STATUS_NORMAL).order_by('-pv')
        else:
            return Post.objects.filter(status=Post.STATUS_NORMAL).order_by('-pv')


    def __str__(self):
        return self.title

    @staticmethod
    def get_by_category(category_id):
        try:
            category = Category.objects.get(id = category_id)
        except category.DoesNotExist:
            post_list = []
            category = None
        else:
            post_list = category.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner', 'category')
        return post_list, category

    @staticmethod
    def get_by_tag(tag_id):
        try:
            tag = Tag.objects.get(id = tag_id)
        except tag.DoesNotExist:
            tag = None
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner','tag')

        return post_list, tag

    @classmethod
    def latest_posts(cls,with_related = True):
        queryset = cls.objects.filter(status = cls.STATUS_NORMAL)
        if with_related:
            queryset = queryset.select_related('owner', 'category')
        return queryset

    def save(self,*args, **kwargs):
        self.content_html = mistune.markdown(self.content)
        super().save(*args, **kwargs)

    @cached_property
    def tagss(self):
        return ','.join(self.tags.values_list('name',flat=True))

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['id']

    class Media:
        css = {
            'all': ("https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css",),
        }
        js = ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js")

