from django.shortcuts import render
from myapp.models import gadb_action, gadb_bill, gadb_legislator, gadb_stats, gadb_vote
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, render_to_response


def index(request):
    return render(request, "index.html")

def home(request):
	return HttpResponse("this is a test")

def gadb_action(request):
	return HttpResponse("votes")

def bill(request):
	bill = gadb_bill.objects.all()
	context = {'bill': bill}
	return render(request,'bills.html',context)

# def bill(request, bill_id):
#     bill = get_object_or_404(gadb_bill, pk=bill_id)
#     return render(request, 'bills.html', {'bill': bill})

def member(request):
	member = gadb_legislator.objects.all()
	context = {'member': member}
	return render (request, 'members.html',context)



def gadb_stats(request):
	return HttpResponse("votes")

def gadb_votes(request):
	return HttpResponse("votes")




