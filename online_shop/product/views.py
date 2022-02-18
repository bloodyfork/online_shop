from django.shortcuts import render


def store(request):
    context = {}
    return render(request, "product/store.html", context)