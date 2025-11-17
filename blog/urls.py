from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('post/new', views.post_new, name="post_new"),
    path('<str:author>/<str:title>', views.post_info, name="post_info"),

]
