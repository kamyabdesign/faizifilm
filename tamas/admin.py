from django.contrib import admin

from . models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    list_display_links = ('name', 'subject')


admin.site.register(Contact, ContactAdmin)
