from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from contacts.models import Contacts
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    return render(request,'accounts/login.html')

def register(request):
    if request.method  == 'POST':
        print(dict(request.POST))
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        password2 = request.POST['password2']
        if password == password2:
            print('_______________________________mwaaaaah__')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User already exists')
                redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'User with same email already exists')
                    redirect('register')
                else:
                    user =User.objects.create_user(username=username,first_name=first_name,last_name=last_name, password= password,email=email)
                    user.save()
                    messages.success(request,'Sucessfully Registered')
                return redirect('login')


        else:
            messages.error(request, 'PASSWORD DO NOT MATCH')
        redirect('register')

    return render(request,'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def dashboard(request):
    user_contacts = Contacts.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {'user_contacts': user_contacts}

    return render(request,'accounts/dashboard.html',context)


