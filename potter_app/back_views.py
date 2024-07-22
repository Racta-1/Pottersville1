from potter_app.models import Category, Gallery, Events
from potter_app.back_forms import UserProfile, CategoryForm, GalleryForm, EventForm
from potter_app.back_forms import LoginForm, RegisterForm, EditUserForm
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from .token import account_activation_token
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, authenticate
from django.utils import timezone
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import(
	ListView, DetailView, UpdateView, DeleteView, CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


@login_required
def dashboard(request):
	cat = Category.objects.count()
	album = Gallery.objects.count()
	event = Events.objects.count()

	dash_dict = {
		"cat": cat,
		"album": album,
		"event": event,
	}
	return render(request, "back/index.html", context=dash_dict)
    
def logout(request):
	return render(request, "back/page-logout.html")


def login_view(request):
	if request.method == "POST":
		#get the posted form
		login_form = LoginForm(data=request.POST)
		if login_form.is_valid():
			#login the user
			user = login_form.get_user()
			login(request, user)
			return redirect('pottersville_app:dashboard')

	else:
		login_form = LoginForm()

	return render(request, 'back/page-login.html', {'form': login_form})


def register(request):

	if request.method == 'POST':
		register_form = RegisterForm(request.POST)

		if register_form.is_valid():
			user = register_form.save(commit=False)
			user.is_active = False
			user.save()
			# messages.success(request, 'Account created successfully')
			current_site = get_current_site(request)

			mail_subject = 'Activate your account.'
			message = render_to_string('back/email_verification.html', {
                            'user': user,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                            'token': account_activation_token.make_token(user)})

			to_email = register_form.cleaned_data.get('email')
			email = EmailMessage(mail_subject, message, to=[to_email])
			email.send()
			return HttpResponse('Please confirm your email address to complete the registration')

		else:
			print(RegisterForm.errors)
	else:
		register_form = RegisterForm()

	return render(request, 'back/page-register.html', context={'form': register_form})


def activate(request, uidb64, token):
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		return redirect('pottersville_app:login')
	else:
		return HttpResponse('Activation link is invalid!')


@login_required
def edit_form(request):
	if request.method == 'POST':
		edit_form = EditUserForm(request.POST, instance=request.user)
		if edit_form.is_valid():
			edit_form.save()
			messages.success(request, 'User edited successfully.')

	else:
		edit_form = EditUserForm(instance=request.user)
	return render(request, 'back/edit-profile.html', {'edit_key': edit_form})


class AddCategory(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = 'back/add-category.html'
	form_class = CategoryForm
	model = Category
	success_url = reverse_lazy('pottersville_app:view-category')
	success_message = "Category added Successfully"


class ListCategory(LoginRequiredMixin, ListView):
	model = Category
	template_name = 'back/view-category.html'
	context_object_name = 'view_cat'


class UpdateCategory(LoginRequiredMixin,SuccessMessageMixin, UpdateView):
	model = Category
	template_name = 'back/add-category.html'
	form_class = CategoryForm
	context_object_name = 'cat'
	success_url = reverse_lazy('pottersville_app:view-category')
	success_message = "Category updated Successfully"


class DeleteCategory(LoginRequiredMixin, DeleteView):
	model = Category
	context_object_name = 'cat'
	success_url = reverse_lazy('pottersville_app:view-category')
	success_message = "Category deleted Successfully"

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(DeleteCategory, self).delete(request, *args, **kwargs)
        
        


class AddEvent(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = 'back/add-event.html'
	form_class = EventForm
	model = Events
	success_url = reverse_lazy('pottersville_app:view-events')
	success_message = "Event added Successfully"


class ListEvent(LoginRequiredMixin, ListView):
	model = Events
	template_name = 'back/view-events.html'
	context_object_name = 'view_events'
	


class UpdateEvent(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Events
	template_name = 'back/add-event.html'
	form_class = EventForm
	context_object_name = 'event'
	success_url = reverse_lazy('pottersville_app:view-events')
	success_message = "Event updated Successfully"


class DeleteEvent(LoginRequiredMixin, DeleteView):
	model = Events
	context_object_name = 'event'
	success_url = reverse_lazy('pottersville_app:view-events')
	success_message = "Event deleted Successfully"

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(DeleteEvent, self).delete(request, *args, **kwargs)


class AddGallery(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = 'back/add-album.html'
	form_class = GalleryForm
	model = Gallery
	success_url = reverse_lazy('pottersville_app:view-album')
	success_message = "Album added Successfully"
	

class ListGallery(LoginRequiredMixin, ListView):
	model = Gallery
	template_name = 'back/view-album.html'
	context_object_name = 'view_album'


class UpdateGallery(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Gallery
	template_name = 'back/add-album.html'
	form_class = GalleryForm
	context_object_name = 'album'
	success_url = reverse_lazy('pottersville_app:view-album')
	success_message = "Album Updated Successfully"


class DeleteGallery(LoginRequiredMixin, DeleteView):
	model = Gallery
	context_object_name = 'album'
	success_url = reverse_lazy('pottersville_app:view-album')
	success_message = "Album Deleted Successfully"

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(DeleteGallery, self).delete(request, *args, **kwargs)
	








