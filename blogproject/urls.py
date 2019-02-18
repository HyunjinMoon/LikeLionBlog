from django.contrib import admin
from django.urls import path
import blogapp.views
import portfolio.views
from django.conf import settings #media쓰기 위해 필요
from django.conf.urls.static import static #외우기 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogapp.views.home,name="home"),
    path('blog/<int:blog_id>',blogapp.views.detail,name="detail"),
    path('blog/new/',blogapp.views.new,name='new'),
    path('blog/create',blogapp.views.create,name='create'),#create함수를 실행시키고 싶어서 만들어줌
    path('portfolio/',portfolio.views.portfolio,name='portfolio'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

