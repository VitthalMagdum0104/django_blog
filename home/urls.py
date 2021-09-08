from django.urls import path
from .views import home, contact, about, handleSignUp, user_login, user_logout, profile

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('signup', handleSignUp, name='signup'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('profile', profile, name='profile'),

]
