from django.shortcuts import render
from django.http import  HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import  price_choices,state_choices,bedroom_choices
# Create your views here.
def index(request):
    listing = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = { 'listing': listing ,
                'price_choices':price_choices,
                'state_choices':state_choices,
                'bedroom_choices':bedroom_choices}


    return render(request,'pages/index.html',context)

def about(request):


    realtors =  Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.filter(is_mvp=True)
    context = {
        'realtors': realtors
    }
    return render(request,'pages/about.html',context)

