from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.homepage, name='app1_homepage'),
    path('about/', views.about, name='app1_about'),  # Add this line
]
