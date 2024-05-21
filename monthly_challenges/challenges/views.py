from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "challenge 1",
    "february": "challenge 2",
    "march": "challenge 3",
    "april": "challenge 4",
    "may": "challenge 5",
    "june": "challenge 6",
    "july": "challenge 7",
    "august": "challenge 8",
    "september": "challenge 9",
    "october": "challenge 10",
    "november": "challenge 11",
    "december": None
}


def monthly_challenge(request, month):
    try:
        text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
                "text": text,
                "month_name": month
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months,
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


# def monthly_challenge(request, month):
#     try:
#         challenge_text = monthly_challenges[month]
#         response_data = f"<h1>{challenge_text}</h1>"
#         return HttpResponse(response_data)
#     except:
#         return HttpResponseNotFound("<h1>Invalid month</h1>")