from django.contrib import admin
from django.urls import path, include
from users.views import home_view

urlpatterns = [
    path('', lambda request: __import__('users.views').views.home_view(request), name='home'),
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
]
