from django import forms
from django.forms import ModelForm
from .models import Profile, Project, Rates


class ProfileForm(forms.ModelForm):
	model = Profile
	username = forms.CharField(label='Username',max_length = 30)
	
	bio = forms.CharField(label='Image Caption',max_length=500)
	profile_pic = forms.ImageField(label = 'Image Field')


class ProfileUploadForm(forms.ModelForm):
	class Meta:
		model = Profile
		
		exclude = ['user']

class ImageForm(forms.ModelForm):
	class Meta:
		model = Project
		
		exclude = ['user']

class ImageUploadForm(forms.ModelForm):
	class Meta:
		model = Project
		
		exclude = ['user']

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        exclude = ['user']
class RatesForm(forms.ModelForm):

    class Meta:
        model = Rates
        exclude = ['overall_score','profile','project']