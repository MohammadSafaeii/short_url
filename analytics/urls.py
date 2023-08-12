from django.urls import path
from . import views


app_name = 'analytics'
urlpatterns = [
    path('url_used/', views.userUrlData, name="general_used"),
]

