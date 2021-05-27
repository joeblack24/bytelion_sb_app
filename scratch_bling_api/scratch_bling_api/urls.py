"""scratch_bling_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.authtoken.views import obtain_auth_token

from back_scratchers.views import HelloView, get_back_scratchers, create_back_scratcher, update_back_scratcher, \
    delete_back_scratchers

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('admin/', admin.site.urls),
    path('get-back-scratchers/', get_back_scratchers, name='all_back_scratchers'),
    path('get-back-scratchers/<str:search_term>', get_back_scratchers, name='get_back_scratchers'),
    path('create-back-scratcher/', create_back_scratcher, name='create_back_scratcher'),
    path('update-back-scratcher/', update_back_scratcher, name='update_back_scratcher'),
    path('delete-back-scratchers/', delete_back_scratchers, name='delete back scratchers'),

]
