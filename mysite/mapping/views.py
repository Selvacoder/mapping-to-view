from django.shortcuts import render

# Home page view
def home_view(request):
    return render(request, 'home.html')

# About page view
def about_view(request):
    return render(request, 'about.html')
