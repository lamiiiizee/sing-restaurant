# Create web/urls.py and paste the following
from django.urls import path
from . import views
from .views import menu
from django.views.generic import TemplateView
app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.about,name='about'),
    path('menu/', views.menu,name='menu'),
    path('gallery/', views.gallery,name='gallery'),
    path('contact/', views.contact,name='contact'),
    path('branch/', views.branch,name='branch'),
    path('single_branch/<int:id>', views.single_branch,name='single_branch'),

]





