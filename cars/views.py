from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Car, Review
from .forms.car_form import CarForm
from .forms.review_form import ReviewForm

import os.path
from uuid import uuid4


def index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})


def add_car(request):
    if request.method == 'GET':
        return render(request, 'cars/change.html')

    elif request.method == 'POST':
        form = CarForm(request.POST)

        if not form.is_valid():
            for field in form:
                for err in field.errors:
                    messages.error(request, str(
                        err).replace('This', field.label))

            return HttpResponseRedirect(reverse('cars:add_car'))

        data = form.cleaned_data

        photo = request.FILES['photo'] if 'photo' in request.FILES else None

        if photo == None:
            messages.error(request, 'A car photo is required.')
            return HttpResponseRedirect(reverse('cars:add_car'))

        photo.name = str(uuid4()) + os.path.splitext(photo.name)[1]

        car = Car(name=data['name'], photo=photo)

        car.save()

        return HttpResponseRedirect(reverse('cars:index'))


def details(request, car_id):
    if request.method == 'GET':
        car = get_object_or_404(Car, pk=car_id)
        return render(request, 'cars/details.html', {'car': car})


def update_car(request, car_id):
    if request.method == 'GET':
        car = get_object_or_404(Car, pk=car_id)
        return render(request, 'cars/change.html', {'car': car})

    elif request.method == 'POST':
        car = get_object_or_404(Car, pk=car_id)

        form = CarForm(request.POST, request.FILES)

        if not form.is_valid():
            for field in form:
                for err in field.errors:
                    messages.error(request, str(
                        err).replace('This', field.label))

            return HttpResponseRedirect(reverse('cars:update_car', args=(car_id,)))

        data = form.cleaned_data

        car.name = data['name']

        photo = request.FILES['photo'] if 'photo' in request.FILES else None

        if photo != None:
            car.photo.delete()
            photo.name = str(uuid4()) + os.path.splitext(photo.name)[1]
            car.photo = photo

        car.save()

        return HttpResponseRedirect(reverse('cars:index'))


def remove_car(request, car_id):
    car = Car.objects.get(pk=car_id)

    car.photo.delete()

    car.delete()

    return HttpResponseRedirect(reverse('cars:index'))


def review(request, car_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if not form.is_valid():
            for field in form:
                for err in field.errors:
                    messages.error(request, str(
                        err).replace('This', field.label))

            return HttpResponseRedirect(reverse('cars:details', args=(car_id,)))

        data = form.cleaned_data

        car = Car.objects.get(pk=car_id)
        car.review_set.create(
            author=data['author'], rating=data['rating'], content=data['content'])

        return HttpResponseRedirect(reverse('cars:details', args=(car_id,)))


def remove_review(request, car_id, review_id):
    Review.objects.filter(pk=review_id).delete()

    return HttpResponseRedirect(reverse('cars:details', args=(car_id,)))
