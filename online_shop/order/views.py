from django.shortcuts import render
from order.models import Cart


def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(customer=customer, is_paid=False)
        items = cart.orderitem_set.all()
    else:
        items = []
    context = {"items": items}
    return render(request, "order/cart.html", context)
