from django.shortcuts import render

from .models import Plan

# Create your views here.

a = 10
def index(request):
    global a
    a -= 1
    plans = Plan.objects.all()
    context = {
        'plans': plans,
        'a': a
    }
    return render(request, 'app/index.html', context=context)