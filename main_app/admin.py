from django.contrib import admin
from .models import Location, Post, Current_City

# Register your models here.
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Current_City)