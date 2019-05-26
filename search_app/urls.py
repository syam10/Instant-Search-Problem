from django.urls import path
from search_app import views

'''
The urlpatterns list routes URLs to views
'''
urlpatterns = [
    path('', views.hello_user, name='home_page'),
    path('search_string', views.get_names, name='search_string'),
    path('results', views.results, name='results'),
]