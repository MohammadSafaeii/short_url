from django.urls import path
from . import views


app_name = 'api'
urlpatterns = [
    path('', views.mainPage, name="main_page"),
    path('make_url', views.makeShortUrl, name="make_short_url"),
    path('r/<str:shorturl>', views.redirection, name="redirection"),
]

