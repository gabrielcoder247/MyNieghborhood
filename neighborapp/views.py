from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .email import send_welcome_email
from .models import *
from .forms import *

# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    # Function to display home page data

    if request.GET.get('search_term'):
        neighborhoods = Neighborhood.search_neighborhood(request.GET.get('search_term'))

    else:
        neighborhoods = Neighborhood.objects.all()


    if request.GET.get('search_term'):
        business = Business.search_business(request.GET.get('search_term'))

    else:
        business = Business.objects.all()


        HttpResponseRedirect('home')


    return render(request, 'index.html', {'businesses':businesses,'neighborhoods':neighborhoods})

def signup(request):
    # Functions for signing up a new user
    
	if request.method == 'POST':

		form = SignUpForm(request.POST, request.FILES)

		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.save()

			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			username = form.cleaned_data.get('email')

			user = authenticate(username =username, password=raw_password, email=email)
			user.save()
			send_welcome_email(username,email)
			login(request, user)

		return redirect('home')

	else:

		form = SignUpForm()

	return render(request, 'signup.html', {"form":form})		



def business(request, id):

    try:
        business = Business.objects.get(pk = id)

    except DoesNotExist:
        raise Http404()

    return render(request, 'business.html', {"business": business})




