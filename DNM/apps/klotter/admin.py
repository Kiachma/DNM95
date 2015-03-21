from django.contrib import admin

from DNM.apps.members.forms import *
from DNM.apps.news.events.models import *
from DNM.apps.klotter.models import *
from DNM.apps.news.models import *
from DNM.apps.static_pages.models import *
from DNM.apps.signup.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

admin.site.register(KlotterPost)
admin.site.register(KlotterVote)

