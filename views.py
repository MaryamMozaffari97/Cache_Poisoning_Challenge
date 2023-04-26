from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

from easy_level.models import Transaction


def get_balance(user):
    balance = cache.get(f"balance_{user.id}")
    if balance is None:
        transactions = Transaction.objects.filter(user=user)
        balance = sum([t.amount for t in transactions])
        cache.set(f"balance_{user.id}", balance)
    return balance


@login_required
def home(request):
    balance = get_balance(request.user)
    message_threshold = 1000
    message_displayed = balance >= message_threshold
    context = {"balance": balance, "message_displayed": message_displayed}
    return render(request, "home.html", context)
