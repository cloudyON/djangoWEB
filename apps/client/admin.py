from django.contrib import admin

from client.models import Product


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(Product, BookmarkAdmin)
# Register your models here.
