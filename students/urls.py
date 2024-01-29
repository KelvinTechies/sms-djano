from django.urls import path
from  .import views



urlpatterns=[
    path("", views.index, name='index'), path('<int:id>', views.view_student, name='view_student'), path('add/', views.add, name='add'), path('edit/<str:pk>/', views.edit, name='edit'), path('delete/<str:pk>/', views.delete, name='delete')];