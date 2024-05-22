from . import views
from django.urls import path

urlpatterns = [
    path('all_cars/', views.show_all_cars),
    path('model/<slug:slug_car>', views.show_one_car, name='car-detail'),
    path('feedback/', views.feedback, name='feedback-name'),
    path('done/', views.done),
]