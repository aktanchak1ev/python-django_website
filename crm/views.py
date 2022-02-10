from django.shortcuts import render
from .models import Order


def first_page(request):
    object_list = Order.objects.all()
    return render(request, './index.html', {'object_list': object_list})


def taken_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(request, './taken_page.html', {'name': name,
                                                 'phone': phone})
