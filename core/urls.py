from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('setting', views.setting, name='setting'),
    path('profile', views.profile, name='profile'),
    path('signout', views.signout, name='signout'),
]


