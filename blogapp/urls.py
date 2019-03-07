from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>',views.detail,name="detail"),
    path('new/',views.new,name='new'),
    path('create',views.create,name='create'),#create함수를 실행시키고 싶어서 만들어줌
]