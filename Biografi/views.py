

# Create your views here.
from django.shortcuts import render
from .models import Bio

# Create your views here.
def Biografi(request):
    Biografi = Bio.objects.all()
    return render(request, "biografi/about.html", {'Biografi':Biografi})