from django.shortcuts import render

def homepage(request):
    return render(request, 'app2/home.html')  # Ensure this template exists