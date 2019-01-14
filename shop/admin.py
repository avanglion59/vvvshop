from django.contrib import admin

from .models import Category, Item, ItemImage


class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 3
    verbose_name = 'картинка товаров'
    verbose_name_plural = 'картинки товаров'


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    inlines = [ItemImageInline]


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
