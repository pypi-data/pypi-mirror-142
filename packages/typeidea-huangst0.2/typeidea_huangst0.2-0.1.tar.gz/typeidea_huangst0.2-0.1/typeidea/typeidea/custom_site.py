from django.contrib.admin import AdminSite

class CustomSide(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea后台管理系统'
    index_title = "首页"
custom_site = CustomSide(name= 'cus_admin')
