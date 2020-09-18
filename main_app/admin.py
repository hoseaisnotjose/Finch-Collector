from django.contrib import admin
# add feeding to the import
from .models import Finch, Feeding
# import models here
from .models import Finch

# Register your models here.
admin.site.register(Finch)
# register feeding model
admin.site.register(Feeding)