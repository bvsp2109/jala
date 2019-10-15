from django.contrib import admin
from .models import JALAModel
from JalaApp import forms
# Register your models here.
class JALAAdmin(admin.ModelAdmin):
    model=JALAModel
    list_display = ['First_Name','Last_Name', 'Email_id','Location','Massage',]
    search_fields = ['First_Name','Last_Name', 'Email_id','Location','Massage',]
admin.site.register(JALAModel, JALAAdmin)