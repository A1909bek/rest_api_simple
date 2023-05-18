from django.urls import path
from .views import toy_detail,toy_list

urlpatterns = [
    path('',toy_list),
    path('<int:pk>/',toy_detail)
]
