from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	return render(request,'restaurantes/home.html',{})

def home(request):
	return render(request,'restaurantes/home.html',{})

def restaurantes(request):
	return render(request,'restaurantes/restaurantes.html',{})

