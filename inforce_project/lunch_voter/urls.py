from django.urls import path
from .views import CreateRestaurantView, UploadMenuView, CreateEmployeeView, CurrentDayMenuView, CurrentDayResultsView

urlpatterns = [
    path('create_restaurant/', CreateRestaurantView.as_view(), name='create_restaurant'),
    path('upload_menu/', UploadMenuView.as_view(), name='upload_menu'),
    path('create_employee/', CreateEmployeeView.as_view(), name='create_employee'),
    path('current_day_menu/', CurrentDayMenuView.as_view(), name='current_day_menu'),
    path('current_day_results/', CurrentDayResultsView.as_view(), name='current_day_results'),
]
