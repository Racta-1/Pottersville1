from django.contrib import admin
from potter_app.models import Category, Events, Gallery
# Register your models here.

admin.site.register(Category)
admin.site.register(Gallery)
admin.site.register(Events)
