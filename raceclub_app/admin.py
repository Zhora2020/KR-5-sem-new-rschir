from django.contrib import admin
from .models import RaceClub, User, Characteristic, Feedback
from django.db.models import QuerySet


admin.site.register(User)


admin.site.register(Feedback)


admin.site.register(Characteristic)


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'car_rating'

    def lookups(self, request, model_admin):
        return  [
            ('<2', 'Низкий'),
            ('от 2 до 2.9', 'Средний'),
            ('от 3 до 3.9', 'Высокий'),
            ('от 4 до 5', 'Наивысший'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value()=='<2':
            return queryset.filter(car_rating__lt=2)
        if self.value()=='от 2 до 2.9':
            return queryset.filter(car_rating__gte=2).filter(car_rating__lt=3)
        if self.value()=='от 3 до 3.9':
            return queryset.filter(car_rating__gte=3).filter(car_rating__lt=4.1)
        if self.value() == 'от 4 до 5':
            return queryset.filter(car_rating__gte=4.1)
        return queryset


@admin.register(RaceClub)
class RaceClubAdmin(admin.ModelAdmin):
    #fields = ['car_name', 'car_rating']
    exclude = ['slug']
    list_display = ['car_name', 'characteristic', 'car_price', 'car_rating', 'car_overclocking', 'car_drive_unit', 'car_transmission', 'slug']
    list_editable = ['car_price', 'characteristic', 'car_rating', 'car_overclocking', 'car_drive_unit', 'car_transmission', 'slug']
    search_fields = ['car_name', 'car_rating']
    list_filter = [RatingFilter]
# Register your models here.