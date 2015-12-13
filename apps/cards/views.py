from django.shortcuts import render


def create_card(request):
    context = {
        "page": "Create your cards here",
        "titles": "Create Card",
    }

    return render(request, "cards/create_card.html", context)


def get_cards(request):
    context = {
        "page": "You can view all your cards here",
        "titles": "Your Cards",
    }

    return render(request, "cards/get_cards.html", context)


def view_card(request):
    context = {
        "page": "View your individual cards here",
        "titles": "Card",
    }

    return render(request, "cards/view_card.html", context)
