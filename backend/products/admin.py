from django.contrib import admin
from .models import Product, ProductImage, Category

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ["image"]
    ordering = ("is_primary", "sort_order")
    show_change_link = True

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["category", "name", "price", "in_stock", "stock_qty", "created_at"]
    list_filter = ["category", "in_stock", "badge"]
    search_fields = ["name", "slug", "sku"]
    inlines = [ProductImageInline]
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "order"]
    search_fields = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}