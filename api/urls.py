from django.urls import path

from . import views

urlpatterns = [
    path('tokens/', views.get_cryptocurrency_info),
    path('test/', views.get_cryptocurrency_test),
]