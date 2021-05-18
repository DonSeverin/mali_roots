from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from voicesystem.models import (Account, User, Call, Menuoptions, Seed, Tree)

class AccountAdmin(UserAdmin):
    list_display    = ('email', 'first_name', 'last_name','date_joined','last_login', 'is_admin', 'is_staff')
    search_fields   = ('email','first_name','last_name')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('email',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets  = ()

admin.site.register(Account, AccountAdmin)
admin.site.register(User)
admin.site.register(Call)
admin.site.register(Menuoptions)
admin.site.register(Seed)
admin.site.register(Tree)
