from django.contrib import admin

# Register your models here.

from .models import ward, alderman, bill, vote

admin.site.register(ward)
admin.site.register(alderman)
admin.site.register(bill)
admin.site.register(vote)
