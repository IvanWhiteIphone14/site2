from uuid import uuid4

from django.contrib import admin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from static.theme_material_kit.utils import send_email
from .models import Car


# Create your views here.
def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        car = request.POST.get('car')
        print(f'Name: {name}, Phone: {phone}, car: {car}')
        subject = 'New Client'
        message = f'Name: {name}\nPhone: {phone}\nCar Model: {car}'
        from_email = 'sales@masterpiecevintage.com'  # Use your Titan Mail email address
        recipient_list = 'sales@masterpiecevintage.com'  # Replace with the recipient's email address

        # Call the send_email function to send the email
        send_email(from_email, 'numberone123123ana.', recipient_list, subject, message)

        # Process or store the data as needed.

        # Return a JSON response with a success message.
        return redirect('main')  # 'main' should be the name of the URL pattern for your main page

    # Return a JSON response for invalid requests.
    return JsonResponse({'message': 'Invalid request'})


def index(request):
    cars = Car.objects.all()
    # Create a dictionary to store cars grouped by brand
    cars_by_brand = {}
    cars_by_type = {}
    brands = list(cars_by_brand.keys())
    types = list(cars_by_type.keys())

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        # Process or store the name and phone number as needed.
        # In this example, we'll just set a session flag to indicate that the form has been submitted.
        request.session['form_submitted'] = True

        # Redirect back to the main page after form submission
        return redirect('main_page')

    for car in cars:
        brand = car.brand
        type = car.type

        if brand not in cars_by_brand:
            cars_by_brand[brand] = []
        cars_by_brand[brand].append(car)

        if type not in cars_by_type:
            cars_by_type[type] = []
        cars_by_type[type].append(car)

    # Check if the form has already been submitted in the session
    if request.session.get('form_submitted', False):
        # If the form has been submitted, render the page without the form
        return render(request, 'pages/index.html',
                      {'brands': brands, 'types': types, 'cars_by_brand': cars_by_brand, 'car_list': cars,
                       'cars_by_type': cars_by_type})

    return render(request, 'pages/index.html',
                  {'brands': brands, 'types': types, 'cars_by_brand': cars_by_brand, 'car_list': cars,
                   'cars_by_type': cars_by_type})


def feedbackurl(request):
    return render(request, '/feedback.html')


def copyindex(request):
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

    return render(request, 'main.html',
                  {'brands': brands, 'types': types, 'cars_by_brand': cars_by_brand, 'car_list': cars,
                   'cars_by_type': cars_by_type})


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
