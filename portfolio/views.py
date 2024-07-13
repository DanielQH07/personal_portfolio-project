from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    projects = Project.objects.all() # Get all the projects from the database
    return render(request, 'portfolio/home.html',{'projects':projects}) # Render the home.html template