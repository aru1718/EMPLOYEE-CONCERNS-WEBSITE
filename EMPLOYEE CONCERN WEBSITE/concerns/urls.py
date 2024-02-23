from django.urls import path
from . import views

urlpatterns = [
    path('', views.concerns_list, name='concerns_list'),
    path('create/', views.create_concern, name='create_concern'),
    path('<int:pk>/delete/', views.delete_concern, name='delete_concern'),
]
