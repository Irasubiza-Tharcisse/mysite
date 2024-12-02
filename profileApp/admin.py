from django.contrib import admin
from .models import project, contact,about,address
# Register your models here.
admin.site.register(project)
admin.site.register(contact)
admin.site.register(about)
admin.site.register(address)