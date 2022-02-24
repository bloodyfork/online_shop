from django.shortcuts import render

from customer.models import Customer
from order.models import Cart


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # customer = Customer.objects.get_or_create(user=request.user)
        cart, created = Cart.objects.get_or_create(customer=customer, is_paid=False)
        items = cart.orderitem_set.all()
        context = {"items": items, "cart": cart}


    else:

        items = []
        context = {"items": items}
    return render(request, "order/cart.html", context)
