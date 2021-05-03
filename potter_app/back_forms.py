
# Importing forms in django


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserChangeForm
from potter_app.models import Category, Gallery, Events, UserProfile


class LoginForm(AuthenticationForm):
	username = forms.CharField(label='', widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
	password = forms.CharField(label='', widget=forms.PasswordInput(
		attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))



class UserForm(UserCreationForm):
	first_name = forms.CharField(widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}), help_text='Required')
	last_name = forms.CharField(widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}), help_text='Required')
	username = forms.CharField(widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
	email = forms.EmailField(widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': 'you@example.com'}), help_text='Required')

	class Meta():
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')


class RegisterForm(UserCreationForm):
	first_name = forms.CharField(label='', widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))
	last_name = forms.CharField(label='', widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
	username = forms.CharField(label='', widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
	email = forms.EmailField(label='', widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': 'you@example.com'}))
	password1 = forms.CharField(label='', widget=forms.PasswordInput(
		attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
	password2 = forms.CharField(label='', widget=forms.PasswordInput(
		attrs={'class': 'form-control', 'placeholder': 'Enter Password Again'}))

	class Meta():
		model = User
		fields = ('username', 'first_name', 'last_name',
		          'email', 'password1', 'password2')


class EditUserForm(UserChangeForm):
	first_name = forms.CharField(widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}), help_text='Required')
	last_name = forms.CharField(widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}), help_text='Required')
	username = forms.CharField(widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
	email = forms.EmailField(widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': 'you@example.com'}), help_text='Required')
	password = None

	class Meta():
		model = UserProfile	
		fields = ('username', 'first_name', 'last_name', 'email')


class CategoryForm(forms.ModelForm):
	cat_name = forms.CharField(label="Name",
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	cat_desc = forms.CharField(label="Description",
		widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta():
		model = Category
		fields = ('cat_name', 'cat_desc')


class EventForm(forms.ModelForm):
	name = forms.CharField(label="Name",
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	desc = forms.CharField(label="Description",
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	image = forms.ImageField(label="Image",
		widget=forms.FileInput(attrs={'class': 'form-control'}))
	date_created = forms.DateField(label="Date of Event",
		widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
	time_created = forms.TimeField(label="Time of Event",
		widget=forms.TimeInput(attrs={'class': 'form-control'}))

	class Meta():
		model = Events
		fields = ('name', 'desc', 'image',
		          'date_created', 'time_created')



class GalleryForm(forms.ModelForm):
	name = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	category = forms.ModelChoiceField(queryset=Category.objects.all(),
		widget=forms.Select(attrs={'class': 'form-control'}))
	gallery_img = forms.ImageField(label="Image",
		widget=forms.FileInput(attrs={'class': 'form-control'}))
	date_created = forms.DateField(
		widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    
        

	class Meta():
		model = Gallery
		fields = ('name', 'category', 'gallery_img', 'date_created')


