from django.shortcuts import render

def homepage(request):
    return render(request, 'app1/home.html')  # Ensure this template exists

def about(request):
    return render(request, 'app1/about.html')  # Ensure this template exists
