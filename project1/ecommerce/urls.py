from django.urls import path
from .views import *

urlpatterns = [
    path('users/',UserView.as_view()),
    path('products/',ProductView.as_view()),
    path('categories/',CategoriesView.as_view()),
    path('user-update/<int:pk>',UpdateUserView.as_view()),
    path('user-delete/<int:pk>',DeleteUserView.as_view()),
    path('user-create/',CreateUserView.as_view()),
]