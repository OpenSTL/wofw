from django.shortcuts import render

# Create your views here.

def index(request):
    return wards(request)

def wards(request):
    return placeholder_list_of("wards")

def ward_detail(request, ward_id):
    return placeholder_detail_on("ward " + str(ward_id))

def aldermen(request):
    return placeholder_list_of("aldermen")

def alderman_detail(request, alderman_name):
    return placeholder_detail_on("alderman " + alderman_name)

def bills(request):
    return placeholder_list_of("bills")

def bill_detail(request, bill_id):
    return placeholder_detail_on("bill " + str(bill_id))



# helpers
def placeholder_list_of(things):
    return("You're looking at a list of all the " + things)

def placeholder_detail_on(thing_description):
    return("You're looking at detail on " + thing_description)
