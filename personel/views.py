from django.shortcuts import render
from django.http import HttpResponse
# from .models import contact_form

def index(request):
	return render(request,"index.html")

def details(request):
	return render(request,"details.html")

def portfolio(request):
	return render(request,"portfolio.html")