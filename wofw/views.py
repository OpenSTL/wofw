from django.shortcuts import render


from django.http import HttpResponse

# Create your views here.
from wofw.models import Ward, Alderman, Vote, Bill



def index(request):
    return wards(request)


def wards(request):
    wards_list = Ward.objects.order_by('-wardnumber')[:Ward.totalCount]
    context = {'wards_list': wards_list}

    return render(request, 'wards.html', context)



def ward_detail(request, wardnumber):
    aldermen_list = Alderman.objects.filter(ward__wardnumber = wardnumber)
    context = {'aldermen_list': aldermen_list}

    return render(request, 'ward_detail.html', context)



def aldermen(request):
    return placeholder_list_of("aldermen")


def alderman_detail(request, alderman_name):
    vote_list = Vote.objects.filter(alderlast__alderlast = alderman_name)
    alderman = Alderman.objects.get(alderlast = alderman_name)

    context = {'vote_list': vote_list, 'alderman': alderman}

    return render(request, 'alderman_detail.html', context)

def bills(request):
    bills_list = Bill.objects.order_by('billnumber')
    context = {'bills_list': bills_list}
    return render(request, 'bills.html', context)


def bill_detail(request, billnumber):
    vote_list = Vote.objects.filter(billnumber__billnumber = billnumber)
    bill = Bill.objects.get(billnumber = billnumber)

    aye_count = Vote.objects.filter(billnumber__billnumber = billnumber, vote = 'aye').count()
    nay_count = Vote.objects.filter(billnumber__billnumber = billnumber, vote = 'nay').count()
    present_count = Vote.objects.filter(billnumber__billnumber = billnumber, vote = 'present').count()
    novote_count = Vote.objects.filter(billnumber__billnumber = billnumber, vote = 'no vote').count()

    context = {'bill': bill, 'vote_list': vote_list, 'aye_count': aye_count, 'nay_count': nay_count, 'present_count': present_count, 'novote_count': novote_count}



    return render(request, 'bill_detail.html', context)


# helpers
def placeholder_list_of(things):
    return HttpResponse("You're looking at a list of all the " + things)


def placeholder_detail_on(thing_name, thing_value):
    return HttpResponse("You're looking at detail on " + thing_name + " " + thing_value)


