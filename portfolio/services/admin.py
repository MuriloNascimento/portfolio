from django.contrib import admin
from portfolio.services.models import Service


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "value")
    list_filter = ("name", "value")


admin.site.register(Service, ServiceAdmin)
