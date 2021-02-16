from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('arts/art-<int:art_id>/', views.art_page, name='art_page'),
    path('about', views.about_page, name='about_page'),
    path('contact', views.contact, name='contact'),
    path('category-<int:cat_id>/', views.category_page, name='category_page'),
]
