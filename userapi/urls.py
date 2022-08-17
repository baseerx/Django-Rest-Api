from rest_framework.decorators import api_view
from rest_framework.response import Response  # for returning json data
from rest_framework.reverse import reverse  # for generating urls
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

urlpatterns = [
    path('all/', views.index, name='all'),
    path('create/', views.create, name='create'),
    path('find/<str:pk>/', views.userDetail, name='find'),
    path('delete/<str:pk>/', views.userDelete, name='delete'),
    path('update/<str:pk>/', views.userUpdate, name='update'),
    path('api-token-auth/', obtain_auth_token,name='api_token_auth'),  # <-- And here

]
