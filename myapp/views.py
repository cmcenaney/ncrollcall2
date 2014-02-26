from django.shortcuts import render
from myapp.models import gadb_action, gadb_bill, gadb_legislator, gadb_stats, gadb_vote
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")

def home(request):
	return HttpResponse("this is a test")

def gadb_action(request):
	return HttpResponse("votes")

def gadb_bill(request):
	return render(request, "bills.html")

def gadb_legislator(request):

	return render(request, "members.html")

def gadb_stats(request):
	return HttpResponse("votes")

def gadb_votes(request):
	return HttpResponse("votes")