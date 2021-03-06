from django.urls import path, include
from . import views

app_name = 'article'

urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),
    # 文章详情
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    # 新建文章
    path('article-create/', views.article_create, name='article_create'),
	# 删除文章
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    # 安全删除文章
    path('article-safe-delete/<int:id>/', views.article_safe_delete, name='article_safe_delete'),
    # 修改文章
    path('article-update/<int:id>/', views.article_update, name='article_update'),
]
