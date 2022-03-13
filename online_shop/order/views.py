from django.views.generic import TemplateView
from django.shortcuts import render
from order.models import Cart


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer=customer, is_paid=False)
        items = cart.orderitem_set.all()

        context = {"items": items, "cart": cart}

    else:
        # ToDO make it for not registered users#
        items = []
        context = {"items": items}
    return render(request, "order/cart.html", context)
