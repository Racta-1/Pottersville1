# Importing forms in django


from django import forms
from potter_app.models import Category, Events

class RegisterForm(forms.Form):
	name = forms.CharField(label='Enter Your Name', required=True, widget=forms.TextInput(
		attrs={'class': 'form-group', 'placeholder': 'Your Name','type':'text',}))
	from_email = forms.EmailField(label="Enter Your Email", required=True, widget=forms.TextInput(
		attrs={'class': 'form-group', 'placeholder': 'Your Email', 'type': 'email'}))
	message = forms.CharField(label='Type Your Messages',required=True, widget=forms.Textarea(
		attrs={'class': 'form-group', 'placeholder': 'I would like to talk to...'}))


