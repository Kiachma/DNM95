from django.contrib import admin

from DNM.apps.news.models import *
from DNM.apps.signup.models import *


admin.site.register(User)
admin.site.register(Grad)
admin.site.register(Title)


