from django.contrib import admin
from .models import Car, CarPhoto


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price', 'year', 'type', 'main_photo', 'short_info')
    list_filter = ('brand', 'model', 'year', 'type')
    search_fields = ('brand', 'model')

    actions = ['delete_selected_cars']

    def delete_selected_cars(self, request, queryset):
        for car in queryset:
            car.delete()

    delete_selected_cars.short_description = "Delete selected cars"


admin.site.register(Car, CarAdmin)
admin.site.register(CarPhoto)
