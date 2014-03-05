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

def member(request):
	member = gadb_legislator.objects.all()
	context = {'member': member}
	return render (request, 'members.html',context)

def each_member(request,pk):
	each_member = get_object_or_404(gadb_legislator, legislator_id=pk)
	return render(request, "eachmember.html", {'each_member': each_member})


	# each_member = gadb_legislator.objects.all()
	# context = {'each_member': each_member}
	# return render (request, 'eachmember.html',context)

def gadb_stats(request):
	return HttpResponse("votes")

def gadb_votes(request):
	return HttpResponse("votes")




