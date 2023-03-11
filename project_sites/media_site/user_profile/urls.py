from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_profile,name='user_profile'),
    path('user_personal_data/',views.user_personal_data,name='user_data'),
    # path('edit/',views.edit,name='edit'),
    path('edit_content/',views.edit,name='edit'),
]