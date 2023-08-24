from django.contrib import admin
from .models import Policy,Client,Reminder

# Register your models here.
admin.site.register(Client)
admin.site.register(Reminder)
admin.site.register(Policy)