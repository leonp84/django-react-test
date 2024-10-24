from django.shortcuts import render


def home(request):
    template = 'testapp/index.html'
    context = {}
    return render(request, template, context)
