from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "no fap",
    "febraury": "no eat"
}


def january(request):
    return HttpResponse("[O]")


def february(request):
    return HttpResponse("Non fap")


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    print(len(months))

    if month > len(months):
        return HttpResponseNotFound()

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):

    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponse(month + " this month is not supported")
