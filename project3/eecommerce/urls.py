from django.urls import path
from .views import UserApiView,ProductApiView,CategoriesApiView,CreateListUserView,CreateListCategoryView,CreateListProductView,UpdateListSignsView,UpdateListCategoryView,UpdateListProductView


urlpatterns = [
    path('users/',UserApiView.as_view()),
    path('categories/',CategoriesApiView.as_view()),
    path('products/',ProductApiView.as_view()),
    path('users/create/',CreateListUserView.as_view()),
    path('categories/create/',CreateListCategoryView.as_view()),
    path('products/create/',CreateListProductView.as_view()),
    path('users/update/<int:pk>/',UpdateListSignsView.as_view()),
    path('categories/update/<int:pk>/',UpdateListCategoryView.as_view()),
    path('products/update/<int:pk>/',UpdateListProductView.as_view()),

]