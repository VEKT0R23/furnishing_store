from django.contrib import admin
from .models import Feedback, ShopGallery, Kitchen, Wardrobe, SleepingRoom, Childish, Material, Blog


# Register your models here.
@admin.register(Kitchen)
class Kitchen(admin.ModelAdmin):
    list_display = ['image', 'image_img', 'description']
    list_editable = ['description']
    list_per_page = 20


@admin.register(Wardrobe)
class Wardrobe(admin.ModelAdmin):
    list_display = ['image', 'image_img', 'description']
    list_editable = ['description']
    list_per_page = 20


@admin.register(SleepingRoom)
class SleepingRoom(admin.ModelAdmin):
    list_display = ['image', 'image_img', 'description']
    list_editable = ['description']
    list_per_page = 20


@admin.register(Childish)
class Childish(admin.ModelAdmin):
    list_display = ['image', 'image_img', 'description']
    list_editable = ['description']
    list_per_page = 20


@admin.register(Material)
class Material(admin.ModelAdmin):
    list_display = ['image', 'image_img', 'description']
    list_editable = ['description']
    list_per_page = 20


@admin.register(ShopGallery)
class ShopGallery(admin.ModelAdmin):
    list_display = ['image', 'image_img', 'name']
    list_editable = ['name']


@admin.register(Feedback)
class Feedback(admin.ModelAdmin):
    list_display = ['name', 'phone_number']


@admin.register(Blog)
class Blog(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'text']

