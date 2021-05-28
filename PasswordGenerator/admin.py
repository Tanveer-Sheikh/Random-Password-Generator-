from django.contrib import admin
from .models import Private
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('datetime',)

    
    
    
admin.site.register(Private,AccountAdmin)
