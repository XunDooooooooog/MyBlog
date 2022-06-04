from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    # 通知列表
    path('list/', views.CommentNoticelistView.as_view(), name='list'),
    # 更新通知列表
    path('update/', views.CommentNoticeUpdateView.as_view(), name='update'),
]