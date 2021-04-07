from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(PrivateDisc)
admin.site.register(Bin)
admin.site.register(Directory)
admin.site.register(File)
admin.site.register(PublicLink)
