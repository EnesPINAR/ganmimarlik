from django.shortcuts import render
from . import models


# Create your views here.
def about(request):
    hakkinda = models.Hakkinda.objects.first()
    context = {
        'hakkinda': hakkinda,
    }
    return render(request, 'about.html', context)