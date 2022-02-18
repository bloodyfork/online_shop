from django.shortcuts import render

# Create your views here.

def cart(request):
    context = {}
    return render(request, "order/cart.html", context)
