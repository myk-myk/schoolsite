from django.contrib import admin

# Register your models here.
from .models import BlogPost, MyUser

admin.site.register(BlogPost)
admin.site.register(MyUser)
