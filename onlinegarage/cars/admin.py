from django.contrib import admin
from django import forms
from cars.models import Car, Review

admin.AdminSite.site_title = 'Online Garage'
admin.AdminSite.site_header = 'Online Garage Adminitration'


class ReviewInline(admin.StackedInline):
    model = Review
    extra = 1


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]

    list_display = ('name', 'id')

    fieldsets = [
        (None, {'fields': ['name']}),
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Car', {'fields': ['car_id']}),
        ('Content', {'fields': ['author', 'content', 'rating']}),
    ]
