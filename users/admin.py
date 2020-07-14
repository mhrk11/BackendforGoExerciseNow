from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=['email', 'username', 'age', 'is_staff']

admin.site.register(CustomUser, CustomAdmin)


# Register your models here.
