from django.contrib import admin
from .models import UserAccount
# Register your models here.


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'email', )
    search_fields = ('email',)
    

admin.site.register(UserAccount, UserAccountAdmin)