# info/admin.py
from django.contrib import admin

from .models import FAQ, Quote

# Register your models here.


admin.site.register(Quote)
admin.site.register(FAQ)
