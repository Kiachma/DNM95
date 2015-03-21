from django.contrib import admin

from DNM.apps.signup.models import *


class CheckboxXSignUpInline(admin.TabularInline):
    model = CheckboxXSignUp


class TextFieldXSignupInline(admin.TabularInline):
    model = TextFieldXSignup




class SignupAdmin(admin.ModelAdmin):
    inlines = [
        CheckboxXSignUpInline, TextFieldXSignupInline,
    ]

admin.site.register(SignUp, SignupAdmin)