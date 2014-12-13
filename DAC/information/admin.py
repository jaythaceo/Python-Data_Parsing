from django.contrib import admin

# Register your models here.
from .models import Information

class SignUpadmin(admin.ModelAdmin):
    class Meta:
        model = Information

admin.site.register(Information, SignUpadmin)

