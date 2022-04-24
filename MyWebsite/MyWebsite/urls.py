"""
Definition of urls for MyWebsite.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('shops/', views.shops, name='shops'),
    path('review/', views.review, name='review'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Вход в аккаунт',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('blogs/', views.blogs, name='blogs'),
    path('videos/', views.videos, name='videos'),
    path('create', views.create, name='create'),
    path('<int:Blog_id>/update', views.Update.as_view(), name='update'),
    path('<int:Blog_id>/', views.blog_itself, name='blog_itself'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

