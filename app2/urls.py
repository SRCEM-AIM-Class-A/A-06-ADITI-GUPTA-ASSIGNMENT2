from django.urls import path
from .views import homepage  # Ensure homepage view exists in app2.views

urlpatterns = [
    path('', homepage, name='app2_homepage'),
]