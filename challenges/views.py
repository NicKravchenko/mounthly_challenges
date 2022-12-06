from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def january(request):
    return HttpResponse("[O]")


def february(request):
    return HttpResponse("Non fap")


def mounthly_challenge_by_number(request, month):
    return HttpResponse(month)


def mounthly_challenge(request, month):
    challenge_text = None

    if month == "july":
        return HttpResponse("o " + month)
    else:
        return HttpResponse(month + " this month is not supported")
