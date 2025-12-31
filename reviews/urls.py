from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.review_list, name='review_list'),
    path('delete/<int:pk>/', views.delete_review, name='delete_review'),
]