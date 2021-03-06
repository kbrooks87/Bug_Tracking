from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from myuser.models import MyUser
# Register your models here.
class MyUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'position',
                ),
            },
        ),
    )

admin.site.register(MyUser, MyUserAdmin)
