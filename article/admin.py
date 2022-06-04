from django.contrib import admin
# 别忘记添加ArticlerPost
from .models import ArticlePost
from .models import ArticleColumn
# Register your models here.

# 注册ArticlePost到admin中
admin.site.register(ArticlePost)
admin.site.register(ArticleColumn)