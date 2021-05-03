from django.shortcuts import render
from potter_app.models import Category, Events, Gallery
from .forms import RegisterForm
from django.contrib import messages
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def index(request):
    register_class = RegisterForm
    if request.method == 'POST':
        register = register_class(data=request.POST)
        if register.is_valid():
            name = request.POST.get('name', '')
            from_email = request.POST.get('from_email', '')
            message = request.POST.get('message', '')

            template = get_template('front/contact.html')
            context = {
                'name': name,
                'from_email': from_email,
                'message': message,
            }
            content = template.render(context)
            email = EmailMessage(
                "New Contact form Submission",
                content,
                "www.pottersville.com.ng" + '',
                ['pottersvilleprivateschool@gmail.com'],
                headers={'Reply-To': from_email}
            )
            email.send()
            messages.success(request, "EMAIL SENT SUCCESSFULLY")
            return redirect('index')
        else:
            messages.error(request, "INVALID FORM INPUT")
    show_event = Events.objects.all()

    index_dict = {
        'title': 'Pottersville Private School',
        'form': register_class,
        'event_list': show_event,

    }

    return render(request, 'front/index.html', context=index_dict)


def gallery(request):
    show_facilities = Gallery.objects.filter(category__cat_name="Facilities")
    show_music = Gallery.objects.filter(category__cat_name="Musicale")
    show_culture = Gallery.objects.filter(category__cat_name="Culture")
    show_sport = Gallery.objects.filter(category__cat_name="Sports")
    show_other = Gallery.objects.filter(category__cat_name="Others")
    category = Category.objects.all()




    register_class = RegisterForm
    if request.method == 'POST':
        register = register_class(data=request.POST)
        if register.is_valid():
            name = request.POST.get('name', '')
            from_email = request.POST.get('from_email', '')
            message = request.POST.get('message', '')

            template = get_template('front/contact.html')
            context = {
                'name': name,
                'from_email': from_email,
                'message': message,
            }
            content = template.render(context)
            email = EmailMessage(
                "New Contact form Submission",
                content,
                "www.pottersville.com.ng" + '',
                ['pottersvilleprivateschool@gmail.com'],
                headers={'Reply-To': from_email}
            )
            email.send()
            messages.success(request, "EMAIL SENT SUCCESSFULLY")
            return redirect('index')
        else:
            messages.error(request, "INVALID FORM INPUT")

    gallery_dict = {
        'title': 'Pottersville Private School',
        'form': register_class,
        'facilities_list': show_facilities,
        'music_list': show_music,
        'culture_list': show_culture,
        'sport_list': show_sport,
        'other_list': show_other,
        'category': category,

    }
    return render(request, 'front/gallery.html', context=gallery_dict)
