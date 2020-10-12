from django.shortcuts import render,redirect
from .models import Contacts
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        realtor_email = request.POST['realtor_email']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        listing = request.POST['listing']
        email = request.POST['email']
        message = request.POST['message']
        print(request.POST)
        contact = Contacts(listing_id=listing_id,name=name,phone_number=phone,user_id=user_id,listing=listing,email=email,message=message)
        contact.save()
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
            'btrealestatechecking@gmail.com',
            [realtor_email, 'khare70@gmail.com'],
            fail_silently=False
        )
        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')




        return redirect('/listings/'+listing_id)
        


