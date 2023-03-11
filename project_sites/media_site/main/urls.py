from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.main,name='main'),
    path('post/<slug:post_slug>/', views.post, name='post'),
    path('registration/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),

]