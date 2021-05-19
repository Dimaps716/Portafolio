from django.urls import path
from . import views

urlpatterns =[
    path('about/', views.Biografi, name="about")
]