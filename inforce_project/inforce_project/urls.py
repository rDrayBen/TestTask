"""inforce_project URL Configuration

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
from django.urls import path, include
from ..lunch_voter.views import CreateRestaurantView, UploadMenuView, CreateEmployeeView, CurrentDayMenuView, CurrentDayResultsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('create_restaurant/', CreateRestaurantView.as_view(), name='create_restaurant'),
    path('upload_menu/', UploadMenuView.as_view(), name='upload_menu'),
    path('create_employee/', CreateEmployeeView.as_view(), name='create_employee'),
    path('current_day_menu/', CurrentDayMenuView.as_view(), name='current_day_menu'),
    path('current_day_results/', CurrentDayResultsView.as_view(), name='current_day_results'),
]
