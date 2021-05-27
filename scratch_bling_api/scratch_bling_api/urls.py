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

from back_scratchers.views import HelloView, GetBackScratchersView, CreateBackScratchersView, UpdateBackScratcherView, \
    DeleteBackScratcherView

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('admin/', admin.site.urls),
    path('get-back-scratchers/', GetBackScratchersView.as_view(), name='all_back_scratchers'),
    path('get-back-scratchers/<str:search_term>', GetBackScratchersView.as_view(), name='get_back_scratchers'),
    path('create-back-scratcher/', CreateBackScratchersView.as_view(), name='create_back_scratcher'),
    path('update-back-scratcher/', UpdateBackScratcherView.as_view(), name='update_back_scratcher'),
    path('delete-back-scratchers/', DeleteBackScratcherView.as_view(), name='delete back scratchers'),

]
