from django.shortcuts import render


# Create your views here.
from musicalapp.models import Instrument


def index(request):
    # it=Instrument()
    # it.name='Guitar'
    # it.desc='Its a String Instrument'
    # it.price=10000
    # it.image='guitar.jpg'
    details=Instrument.objects.all()
    return render(request,'index.html',{'it':details})