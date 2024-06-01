from django.contrib import admin

from .models.shops import Shop

class ShopAdmin(admin.ModelAdmin):
    list_display = [
        "shop_name",
        "first_name",
        "email",
        "is_visible",
        "created_at",
    ]




admin.site.register(Shop, ShopAdmin)
