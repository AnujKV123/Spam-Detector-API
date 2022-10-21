"""checkSpam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns

import users.views
import spam.views

urlpatterns = [
  path('admin/', admin.site.urls),
  
  path('api/all_users/', users.views.userList),
  path('api/create_user/', users.views.setUser),
  path('api/user/<int:id>', users.views.getUser),

  path('api/all_spams/', spam.views.spamLists),
  path('api/report/', spam.views.reportSpam),

  path('api/search/<str:query>', users.views.searchUser),
]

urlpatterns = format_suffix_patterns(urlpatterns)
