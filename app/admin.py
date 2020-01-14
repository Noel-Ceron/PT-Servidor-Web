from django.contrib import admin

from .models import UserInfo
from .models import Pantalla
from .models import Control
from .models import ControlCompleto

admin.site.register(UserInfo)
admin.site.register(Pantalla)
admin.site.register(Control)
admin.site.register(ControlCompleto)
# Register your models here.
