from django.contrib import admin

from store.models import Customer, Product, Category, CartProduct, Cart, Specification, SpecificationsProduct, Brands


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'address',
        'city',
        'region'
    ]


@admin.register(Product)
class ProductdAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'category',
        'brand'
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['owner']


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'products']


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(SpecificationsProduct)
class SpecificationsProductAdmin(admin.ModelAdmin):
    list_display = ['product']


@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('name',)
