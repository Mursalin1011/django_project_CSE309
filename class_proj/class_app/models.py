from django.db import models
from django.contrib import admin


# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Paper Content', blank=True)

    def __str__(self):
        return self.title

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('title',)
    search_fields = ('title',)
    
    def __str__(self):
        return self.list_display