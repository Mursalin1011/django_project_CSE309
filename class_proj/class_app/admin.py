from django.contrib import admin
from .models import Page, PageAdmin
# Register your models here.

# admin.site.register(Page)
admin.site.register(Page, PageAdmin)