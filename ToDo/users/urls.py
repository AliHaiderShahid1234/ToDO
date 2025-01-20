from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('signup/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]
