from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(CustomUSer)
admin.site.register(Category)
admin.site.register(Product)