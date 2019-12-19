from django.contrib import admin

from .models import UserInfo
from .models import Pantalla
from .models import Control

admin.site.register(UserInfo)
admin.site.register(Pantalla)
admin.site.register(Control)
# Register your models here.
