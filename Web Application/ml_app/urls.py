"""project_settings URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import about, index, predict_page,cuda_full,statistics

app_name = 'ml_app'
handler404 = views.handler404

urlpatterns = [
    path('', about, name='about'),
    path('index/', index, name='home'),
    path('predict/', predict_page, name='predict'),
    path('cuda_full/',cuda_full,name='cuda_full'),
    path('statistics/',statistics,name='statistics')
]
