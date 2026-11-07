from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse





def index(request):
    return HttpResponse("Hello, world. You're at the youtube app index.")
def maps(request):
    return render(request, 'maps/maps.html')



