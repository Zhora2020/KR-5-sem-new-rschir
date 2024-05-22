from django.shortcuts import render, get_object_or_404
from .models import RaceClub, Feedback
from django.http import HttpResponseRedirect
from .forms import FeedbackForm


def feedback(request):

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feed = Feedback(
                name=form.cleaned_data['name'],
                nickname=form.cleaned_data['nickname'],
                feedback=form.cleaned_data['feedback'],
                rating=form.cleaned_data['rating'],
            )
            feed.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm()
    return render(request, 'raceclub_app/feedback.html', context={'form': form})


def done(request):
    return render(request, 'raceclub_app/done.html')


def show_all_cars(request):
    cars = RaceClub.objects.order_by('car_name')
    return render(request, 'raceclub_app/all_cars.html', {
        'cars': cars
    })


def show_one_car(request, slug_car: str):
    car = get_object_or_404(RaceClub, slug=slug_car)
    return render(request, 'raceclub_app/one_car.html', {
        'car': car
    })
