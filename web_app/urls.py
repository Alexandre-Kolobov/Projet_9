"""
URL configuration for web_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import authentication.views
import blog.views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (PasswordChangeView, PasswordChangeDoneView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.LoginPageView.as_view(), name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    
    path('change_password/', PasswordChangeView.as_view(template_name='authentication/change_password.html'), 
         name='password_change'), # renvoi par defaut vers "password_change_done"

    path('change_password_done/', PasswordChangeDoneView.as_view(template_name='authentication/change_password_done.html'), 
         name='password_change_done'),

    path('home/', blog.views.home, name='home'),
    path('create_user/', authentication.views.CreateUserView.as_view(), name='create_user'),
    path('home/ticket_creation', blog.views.ticket_creation, name='ticket_creation'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)