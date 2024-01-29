from django.contrib import admin
from .models import person
# Register your models here.

class personAdmin(admin.ModelAdmin):
  list_display = ("username", "fullname","phone","email","password",)


admin.site.register(person,personAdmin)