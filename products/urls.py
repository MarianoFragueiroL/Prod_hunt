
from django.urls import path, include
from . import views

urlpatterns = [

    path('create', views.create, name='create'),
    path('<int:product_id>/', views.details, name= 'prod_details'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
]