from django.contrib import admin
from .models import Article, Author, Category, Tag, Comments, Alls


class AllAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_display_links = ('name', )


admin.site.register(Alls, AllAdmin)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'jpublish')
    list_display_links = ('name', )


admin.site.register(Comments, CommentsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title', )


admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title', )


admin.site.register(Tag, TagAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'jpublish')
    list_filter = ('status', )
    list_display_links = ('title', )
    search_fields = ('title', 'description')


admin.site.register(Article, ArticleAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', )


admin.site.register(Author, AuthorAdmin)
