from django.urls import include, path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('<int:list_id>', views.index, name='index'),
    path('<int:list_id>/', views.list, name='list'),
    path('<int:list_id>/add/', views.add, name='add'),
    path('<int:list_id>/remove/', views.remove, name='remove'),
    path('<int:list_id>/delete/', views.delete, name='delete'),
    path('<int:list_id>/list_only/', views.list_only, name='list_only'),
    path('remove/', views.remove_list, name='remove_list'),
    path('add/', views.add_list, name='add_list'),
]
