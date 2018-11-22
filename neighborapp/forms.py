from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# Create a signup form fields
class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30,  required=False, help_text='Optional.')
    username= forms.CharField(max_length=30,required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
  

    class Meta:
        model = User
        fields = ('username', 'name', 'email',
                  'password1', 'password2')

# Create a profile form fields
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','neighborhood_id'] 
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


# Create a image form fields
class NewImageForm(forms.ModelForm):
	class Meta:
		model = Image
        # exclude = ['user','location'],
		fields = ['name', 'description', 'image','likes','comments']

class CreateNeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['user',]

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','neighborhood_id']        
        
        



# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comments
#         fields = ('comment',)
#         exclude = ['user','post']

# class LikesForm(forms.ModelForm):
#     class Meta:
#         model=Likes
#         exclude=['user']
#         fields=[]         		
