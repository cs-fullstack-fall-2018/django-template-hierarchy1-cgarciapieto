from django.http import HttpResponse

from .models import Blockbuster
from django.shortcuts import render


def index(request):
    latest_blockbuster_list = Blockbuster.objects.all()
    context = {'latest_blockbuster_list': latest_blockbuster_list}
    return render(request, 'movie_app/index.html', context)

def movie(request):
    latest_blockbuster_list = Blockbuster.objects.all()
    context = {'latest_blockbuster_list': latest_blockbuster_list}
    return render(request, 'movie_app/index.html', context)


