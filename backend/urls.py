from django.urls import path

from . import views
app_name='backend'
urlpatterns = [
    path('create/', views.create, name = 'create'),
    path('read', views.read, name = 'read'),
    path('update/', views.update, name = 'update'),
    path('delete/', views.delete, name = 'delete'),
    path('search', views.search, name = 'search')
]