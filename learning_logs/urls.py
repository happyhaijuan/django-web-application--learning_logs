"""  定义learning_logs的URL模式 """
from django.urls import path,re_path
from . import views

app_name = "learning_logs"
urlpatterns = [
        #主页
        path('', views.index, name='index'),
        #显式所有的主题
        path('topics/', views.topics, name = 'topics'),
        #特定主题的详细页面
        re_path(r'^topics/(?P<topics_id>\d+)/$',views.topic, name = 'topic'),
]