from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponse

# Create your views here.
# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'quiz/index.html', {})


def IndexView(request):
    return render(request, 'quiz/index.html', {})


def DetailView(request):
    pass


def ListView(request):
    pass


def CreateView(request):
    pass
