
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('search_bar/<int:page>/', views.store_search_bar),
    path('search/<str:search>/', views.store_search,name="store_search"),
    path('read_more/', views.read_more,name="read_more"),
    path('search/<str:search>/<int:page>/', views.store_search_page,name="store_search_page"),
    path('bookmarks/', views.bookmarks,name='bookmarks'),
    path('bookmarks/add_bookmark/', views.add_bookmark,name = "add_bookmark"),
    path('bookmarks/delete_bookmark/', views.delete_bookmark,name = "delete_bookmark"),
    path('bookmarks/<int:page>/', views.bookmarks_page),
]
