from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
from wofw.models import Ward


def index(request):
    return wards(request)


def wards(request):
    wards_list = Ward.objects.order_by('-wardnumber')[:Ward.totalCount]
    context = {'wards_list': wards_list}

    return render(request, 'wards.html', context)


def ward_detail(request, wardnumber):
    return placeholder_detail_on("ward", wardnumber)


def aldermen(request):
    return placeholder_list_of("aldermen")


def alderman_detail(request, alderman_name):
    return placeholder_detail_on("alderman", alderman_name)



def bills(request):
    return placeholder_list_of("bills")


def bill_detail(request, billnumber):
    return placeholder_detail_on("bill", billnumber)

# helpers
def placeholder_list_of(things):
    return HttpResponse("You're looking at a list of all the " + things)


def placeholder_detail_on(thing_name, thing_value):
    return HttpResponse("You're looking at detail on " + thing_name + " " + thing_value)

