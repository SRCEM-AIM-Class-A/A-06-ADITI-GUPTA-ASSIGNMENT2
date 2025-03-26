from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_app1(request):
    return redirect('/app1/')  # Redirect root URL to app1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),  # Ensure app1 is included
    path('app2/', include('app2.urls')),  # Ensure app2 is included
    path('', redirect_to_app1, name='homepage'),  # Add this line
]