from django.contrib import admin
from behinkar.models import adtitle
class AdminMode(admin.ModelAdmin):
    list_display = ['company_name','state']
admin.site.register(adtitle,AdminMode)

# Register your models here.
