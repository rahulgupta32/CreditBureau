from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question, UserResponse

admin.site.register(Question)
admin.site.register(UserResponse)
