from django.contrib import admin

from .models import Work, Item


class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'jpublish')
    list_display_links = ('title', )
    search_fields = ('title', 'description')


admin.site.register(Work, WorkAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'phone')
    list_display_links = ('address', )


admin.site.register(Item, ItemAdmin)
