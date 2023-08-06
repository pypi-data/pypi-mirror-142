from django.urls import path

from wagtail_colour_picker_enoki.views import chooser


app_name = 'wagtail_colour_picker_enoki'

urlpatterns = [
    path('chooser/', chooser, name='chooser'),
]
