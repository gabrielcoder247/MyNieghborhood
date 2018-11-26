from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from .email import send_welcome_email
from django.urls import reverse
from .models import *
from .forms import *

# Create your views here.


@login_required(login_url='/accounts/login/')
def homePage(request):
    # Function to display home page data

    if request.GET.get('search_term'):
        neighborhoods = Neighborhood.search_neighborhood(request.GET.get('search_term'))

    else:
        neighborhoods = Neighborhood.objects.all()


    if request.GET.get('search_term'):
        business = Business.search_business(request.GET.get('search_term'))

    else:
        business = Business.objects.all()


    
    if request.GET.get('search_term'):
        images = Image.search_image(request.GET.get('search_term'))

    else:
        images = Image.objects.all()

    


        HttpResponseRedirect('home_page')


    return render(request, 'home.html', {'business':business,'neighborhoods':neighborhoods, 'images':images})

def signup(request):
    # View functions for signing up a new user
    
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

		return redirect('home_page')

	else:

		form = SignUpForm()

	return render(request, 'signup.html', {"form":form})		



def business(request, id):

    try:
        business = Business.objects.get(pk = id)

    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'business.html', {"business": business})

def neighborhood(request, id):

    try:
        neighborhood = Neighborhood.objects.get(pk = id)
        business = Business.objects.filter(neighborhood_id=neighborhood)

    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'neighborhood.html', {"neighborhood": neighborhood, 'business':business})


@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.save()
        return redirect('home_page')

    else:
        form = NewBusinessForm()
    return render(request, 'new_business.html', {"form": form})	


@login_required(login_url='/accounts/login/')
def new_neighborhood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewNeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighborhood = form.save(commit=False)
            neighborhood.user = current_user
            neighborhood.save()
        return redirect('home_page')

    else:
        form = NewNeighborhoodForm()
    return render(request, 'create/new_neighborhood.html', {"form": form})

# @login_required(login_url='/accounts/login/')
# def join(request,id):

#     '''
#     This view function will implement adding
#     '''

#     neighborhood_id = get_object_or_404(Neighborhood, pk=id)
#     request.user.neighborhood = neighborhood_id
#     request.user.save()

#     print("success")
#     return redirect(homePage)





@login_required(login_url='/accounts/login/')
def join(request, id):
    '''
    This view function will implement adding
    '''
    neighborhood = Neighborhood.objects.get(pk=id)
    if Join.objects.filter(user_id=request.user).exists():

		

        Join.objects.filter(user_id=request.user).update(neighborhood_id=neighborhood)

        return redirect(reverse('neighborhood', args=(neighborhood.id,)))

    else:

        Join(user_id=request.user, neighborhood_id=neighborhood).save()

    print("success")
    return redirect('home_page')


@login_required(login_url='/accounts/login/')
def exit(request, id):

    neighborhood = Neighborhood.objects.get(pk=id)
    if Join.objects.filter(user_id=request.user).exists():

        Join.objects.filter(user_id=request.user).delete()

        return redirect(reverse('neighborhood', args=(neighborhood.id,)))

    else:

        Join(user_id=request.user, neighborhood_id=neighborhood).delete()

    print("success")
    return redirect('homePage')



# def exit(request,id):
#     neighborhood_id = get_object_or_404(Neighborhood, pk=id)
#     if request.user.neighborhood == neighborhood_id:
#         request.user.neighborhood=None
#         request.user.save()
#     return redirect(homePage)




def search_business(request):

    # search for a business by its name
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_business(search_term)
        message = "{search_term}" 

        return render(request, 'search.html', {"message": message, "business": searched_business})

    else:
        message = "You haven't searched for any business"
    return render(request, 'search.html', {"message": message})


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = UpdatebioForm(request.POST, request.FILES, instance=current_user.profile)
        print(form.is_valid())
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('homePage')

    else:
        form = UpdatebioForm()
    return render(request, 'edit_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('homePage')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})



