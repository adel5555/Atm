from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Customer, Card
from .ATM import end_date_checker
# Create your views here.


def process_for_data_and_card_id(request):
    request.session = dict()
    if request.method == 'POST':
        card_id = request.POST.get('card_id')
        try:
            card = Card.objects.get(card_number=card_id)
            # return render(request,'process_error.html',{"error":card.expire_date})
        except:
            request.session = dict()
            return render(request, 'process_error.html', {"error": "Invalid Card Number"})

        if card.card_status == 1:
            request.session = dict()
            return render(request, 'process_error.html', {"error": "your card is blocked"})
        elif end_date_checker(card.expire_date):
            request.session = dict()
            return render(request, 'process_error.html', {"error": "Invalid Card date is expired "})
        request.session['card_id'] = card_id
        url = reverse('password')
        return redirect(url)

    return render(request, 'process_card.html', {"label": "enter card number"})


def process_for_password(request):
    if 'card_id'not in request.session:
        url = reverse('card_id')
        return redirect(url)
    try:
        card = Card.objects.get(id=request.session['card_id'])
    except:
        request.session = dict()
        return render(request, 'process_error.html', {"error": "Invalid Card Number"})

    if request.method == 'POST':
        card_password = request.POST.get('card_password')
        if card.attempts > 0:
            if card_password == card.password:
                card.attempts = 3
                card.save()
                request.session['login'] = 1
                url = reverse('withdraw')
                return redirect(url)
            else:
                card.attempts -= 1
                card.save()
        if card.attempts == 0:
            card.card_status = 1
            card.save()
            request.session = dict()
            return render(request, 'process_error.html', {"error": "Too many incorrect attempts. Access denied. and your card is blocked"})
        url = reverse('password')
        return redirect(url)

    return render(request, 'process_password.html', {"label": "enter card Password", "try": card.attempts})


def process_for_withdraw(request):
    if 'login'not in request.session:
            url = reverse('card_id')
            return redirect(url)
    if request.method == 'POST':
        card_withdraw = float(request.POST.get('card_withdraw'))
        if not card_withdraw:
            return render(request, 'process_error.html', {"error": "Invalid Card Number"})
        try:
            card = Card.objects.get(card_number=request.session['card_id'])
        except:
            request.session = dict()
            return render(request, 'process_error.html', {"error": "Invalid Card Number"})

        if (card.customer.balance >= card_withdraw or card.customer.neg_allowed) and card.customer.allowed_amount >= card_withdraw:
            card.customer.balance -= card_withdraw
            card.customer.save()
            request.session = dict()
            return render(request, 'process_error.html', {"error": "success"})
        elif card.customer.allowed_amount < card_withdraw:
            return render(request, 'process_error.html', {"error": "too much "})
        else:
            return render(request, 'process_error.html', {"error": "ما عندك كمية يا مطي "})

    return render(request, 'process_withdraw.html', {"label": "enter withdraw"})
