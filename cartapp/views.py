from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from cartapp.models import Cart, Order
from musicalapp.models import Instrument


def removeitems(request,id):
    pass


def addtocart(request, id):
    c = Cart()
    instrumentid = Instrument.objects.get(id=id)
    uid = request.session.get('uid')
    userid = User.objects.get(id=uid)
    c.instrument = instrumentid
    c.user = userid
    c.save()
    messages.info(request, "Cart Added Successfully!")
    return redirect("/")


def cartlist(request):
    uid = request.session.get('uid')
    cr = Cart.objects.filter(user=uid)
    if request.method == "POST":
        totalbill = 0
        qty = int(request.POST['qty'])
        for i in cr:
            totalbill = totalbill + i.instrument.price * qty

        o = Order()
        o.totalBill = totalbill
        o.user = User.objects.get(id=uid)
        o.status = "Completed"
        o.save()
        for i in cr:
            i.delete()

        return render(request, "index.html", {'totalbill': totalbill})


    else:
        d = {'cr': cr}
        return render(request, "cartlist.html", d)
