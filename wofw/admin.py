from django.contrib import admin

# Register your models here.

from .models import Ward, Alderman, Bill, Vote

admin.site.register(Ward)
admin.site.register(Alderman)
admin.site.register(Bill)
admin.site.register(Vote)
