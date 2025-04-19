from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'index.html', context)


def about(request):
    context = {

    }
    return render(request, 'about.html', context)


def credentials(request):
    context = {

    }
    return render(request, 'credentials.html', context)

def services(request):
    context = {

    }
    return render(request, 'services.html', context)

def services_detail(request, pk):
    context = {

    }
    return render(request, 'services_detail.html', context)