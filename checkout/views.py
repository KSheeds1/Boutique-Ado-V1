from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K19ECAQ5HfbhpaVhetQO6caHdfKPZmp4S7kIe1iL1FULdAASrBcWaE9AcaTCrZjMkOtJlTPKmiTz4a3DANICHI800Nvxn4sjt',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

