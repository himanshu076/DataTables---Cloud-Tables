from django.urls import path, include
from server_side_table import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('data/', views.OrderListJson.as_view(), name="api_data"),
    path('data/', views.ApiView.as_view(), name="api"),
]