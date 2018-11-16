from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    # Function to display home page data

    if request.GET.get('search_term'):
        neighborhoods = Neighborhood.search_neighborhood(request.GET.get('search_term'))

    else:
        neighbourhoods = Neighbourhood.objects.all()


    if request.GET.get('search_term'):
        business = Business.search_business(request.GET.get('search_term'))

    else:
        business = Business.objects.all()

    # if request.GET.get('search_term'):
    #     projects = Project.search_project(request.GET.get('search_term'))

    # else:
    #     projects = Project.objects.all()

    # form = NewsLetterForm

    # if request.method == 'POST':
    #     form = NewsLetterForm(request.POST or None)


    #     if form.is_valid():
    #         name = form.cleaned_data['your_name']
    #         email = form.cleaned_data['email']

    #         recipient = NewsLetterRecipients(name=name, email=email)
    #         recipient.save()
    #         send_welcome_email(name, email)

        HttpResponseRedirect('home')


    return render(request, 'index.html', {'projects':projects, 'letterForm':form,
                                          'businesses':businesses,
                                          'neighbourhoods':neighbourhoods})





