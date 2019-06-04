from rest_framework.authtoken.models import Token
from rest_framework.authtoken.admin import TokenAdmin


from django.contrib import admin

# Register your models here.

TokenAdmin.raw_id_fields = ('user',)
