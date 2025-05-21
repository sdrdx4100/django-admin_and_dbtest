from django.contrib import admin
from django.urls import path
from app.views import login_view, login_success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('login_success/', login_success, name='login_success'),
]
