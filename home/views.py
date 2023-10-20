from uuid import uuid4

from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from .models import Car


# Create your views here.
def index(request):
    cars = Car.objects.all()

    # Create a dictionary to store cars grouped by brand
    cars_by_brand = {}

    cars_by_type = {}

    for car in cars:
        brand = car.brand
        type = car.type

        if brand not in cars_by_brand:
            cars_by_brand[brand] = []
        cars_by_brand[brand].append(car)

        if type not in cars_by_type:
            cars_by_type[type] = []
        cars_by_type[type].append(car)

    # Get a list of all unique brand names
    brands = list(cars_by_brand.keys())
    types = list(cars_by_type.keys())

    return render(request, 'pages/index.html',
                  {'brands': brands, 'types': types, 'cars_by_brand': cars_by_brand, 'car_list': cars,
                   'cars_by_type': cars_by_type})


def feedbackurl(request):
    return render(request, '/feedback.html')


class CarAdmin(admin.ModelAdmin):
    # Specify the fields you want to display in the admin form
    list_display = ('brand', 'model', 'price', 'year')

    # Customize the form for adding new listings
    fieldsets = (
        (None, {
            'fields': ('brand', 'model', 'price', 'year', 'main_photo', 'photos', 'short_info')
        }),
    )


def car_details(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        car_photos = car.carphoto_set.all()  # Assuming you haven't customized the related name
    except Car.DoesNotExist:
        # Handle the case where the car with the specified ID does not exist
        # You can return a 404 error page or a custom error message
        return render(request, 'car_not_found.html')

    return render(request, 'car_details.html', {'car': car, 'car_photos': car_photos})
