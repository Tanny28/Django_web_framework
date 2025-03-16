from django.contrib import admin
from .models import Employees
from .models import Menu

admin.site.register(Menu)  # Registers Menu model
admin.site.register(Employees)
