from django.shortcuts import render
from myapp.models import gadb_action, gadb_bill, gadb_legislator, gadb_stats, gadb_vote
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, render_to_response

# from django.views.generic.list import ListView


def index(request):
    bill = gadb_bill.objects.all()
    member = gadb_action.objects.all()
    # action = gadb_action.objects.all()
    action_list = []

    limit = 10
    # count_action = action.count()
    # end_action = action[count_action-limit:]
    count_bill = bill.count()
    end_bill = bill[count_bill-limit:]

   
    for i in end_bill:
    	action = gadb_action.objects.filter(bill_id=i.bill_id)
    	action_list.append(action)

    context = {
    	'action':action,
    	'bill':end_bill,
    	'member':member
    }
    return render(request, "index.html", context)
    #return render(request,"index.html")


#     queryset = Shop.objects.filter(id=someArray[id])
# limit = 1000
# count = queryset.count()
# endoflist = queryset.order_by('timestamp')[count-limit:]

def home(request):
	return HttpResponse("this is a test")

def bill(request):
	bill = gadb_bill.objects.all()
	context = {'bill': bill}
	return render(request,'bills.html',context)

def each_bill(request,bill_id):
	each_bill = get_object_or_404(gadb_bill, bill_id=bill_id)
	action = gadb_action.objects.filter(bill_id=bill_id)

	context = {
		'each_bill': each_bill,
		'action': action
	}
	return render(request, "eachbill.html", context)

def member(request):
	member = gadb_legislator.objects.all()
	context = {'member': member}
	return render (request, 'members.html',context)

def each_member(request,legislator_id):
	each_member = get_object_or_404(gadb_legislator, legislator_id=legislator_id)
	each_vote = gadb_vote.objects.filter(legislator_id=legislator_id)
	# vote = gadb_vote.objects.all()

	context = {
		'each_member': each_member,
		'each_vote': each_vote
	}
	
	return render(request, "eachmember.html", context)




	# all_models_dict = {
 #        "template_name": "eachmember.html",
 #        "queryset": each_member.objects.all(),
 #        "extra_context" : {"vote" : gadb_vote.objects.all(),
 #                           "each_member": get_object_or_404(gadb_legislator, legislator_id=legislator_id)
 #                           #and so on for all the desired models...
 #                           }
 #    }


def gadb_stats(request):
	return HttpResponse("votes")

def gadb_votes(request):
	vote = gadb_vote.objects.all()
	context = {'vote': vote}
	return render(request,'eachbill.html',context)





