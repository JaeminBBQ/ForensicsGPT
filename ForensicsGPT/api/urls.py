from django.urls import path, include
from . import views

urlpatterns = [
    path('llama/', views.query_llama, name="llama"),
]