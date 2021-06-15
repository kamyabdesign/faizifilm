from django.contrib import admin

from . models import Main, Team, Trust, Video, Hestory, our_service, Testimonial, Features


class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('name', 'detail')
    list_display_links = ('name', )


admin.site.register(Features, FeaturesAdmin)


class Our_serviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')
    list_display_links = ('name', )
    search_fields = ('name', 'content')


admin.site.register(our_service, Our_serviceAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')
    list_display_links = ('name', )
    search_fields = ('name', )


admin.site.register(Testimonial, TestimonialAdmin)


class MainAdmin(admin.ModelAdmin):
    list_display = ('title', 'overview')
    list_display_links = ('title', )
    search_fields = ('title', )


admin.site.register(Main, MainAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_display_links = ('name', )
    search_fields = ('name', )


admin.site.register(Team, TeamAdmin)


class HestoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_display_links = ('title', )
    search_fields = ('title', )


admin.site.register(Hestory, HestoryAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title', )
    search_fields = ('title', )


admin.site.register(Video, VideoAdmin)


class TrustAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_display_links = ('title', )
    search_fields = ('title', )


admin.site.register(Trust, TrustAdmin)
