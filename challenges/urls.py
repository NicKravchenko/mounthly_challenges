from django.urls import path

from . import views

urlpatterns = [

    path(r"<int:month>/", views.monthly_challenge_by_number),
    path(r"<str:month>/", views.monthly_challenge, name='month-challenge')
]
