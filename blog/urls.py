from django.urls import path
from .views import bloghome, blogpost, create, delete, edit

urlpatterns = [
    path('', bloghome, name='bloghome'),
    path('<str:slug>', blogpost, name='blogpost'),
    path('<int:serial_no>', delete, name='deleteblog'),
    path('create/', create),
    path('edit/', edit)
]
