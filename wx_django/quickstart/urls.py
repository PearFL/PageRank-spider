from django.urls import path
from .views import wx, menu

urlpatterns = [
    path('hello', wx.helloworld),
    path('weather', wx.weather),
    path('menu', menu.get_menu),

]