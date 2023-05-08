from django.urls import path
from . import views

#開始設定路徑
urlpatterns = [
    path('index', views.index),
    path('cooperation', views.cooperation),
    path('cooperation/image', views.jump),
    path('weather', views.weather),
    path('weather/map', views.global_map),
    path('news', views.news),
]

"""
在path小括號中，
第一個參數是網址列後方所顯示的路徑，
第二個參數是此網頁所對應的函式
"""