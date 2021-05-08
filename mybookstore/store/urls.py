
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('search_bar/<int:page>/', views.store_search_bar),
    path('search/<str:search>/', views.store_search,name="store_search"),
    path('search/<str:search>/<int:page>/', views.store_search_page,name="store_search_page"),
]
