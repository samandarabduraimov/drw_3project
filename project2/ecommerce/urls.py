from django.urls import path
from .views import create_user, get_user,get_user_id,delete_user,update_user,partial_update_user



urlpatterns = [
    path('create_user/',create_user,name='create_user'),
    path('get_user/',get_user,name='get_user'),
    path('get_user/<int:pk>',get_user_id,name='get_user_id'),
    path('delete_user/<int:pk>',delete_user,name='delete_user'),
    path('update_user/<int:pk>',update_user,name='update_user'),
    path('partial_update_user/<int:pk>',partial_update_user,name='partial_update_user'),
]