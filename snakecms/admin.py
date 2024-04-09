from django.contrib import admin
from snakecms.models import Profile


@admin.register(Profile)
class PersonAdmin(admin.ModelAdmin):
    pass
