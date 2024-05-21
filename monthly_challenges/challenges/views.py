from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "challenge.css 1",
    "february": "challenge.css 2",
    "march": "challenge.css 3",
    "april": "challenge.css 4",
    "may": "challenge.css 5",
    "june": "challenge.css 6",
    "july": "challenge.css 7",
    "august": "challenge.css 8",
    "september": "challenge.css 9",
    "october": "challenge.css 10",
    "november": "challenge.css 11",
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