from django.shortcuts import render

from item.models import Category, Items

from .forms import SignupForm ,SigninForm

# Create your views here.




def index(request):
    items = Items.objects.filter(is_sold=False)[:12]
    categories = Category.objects.all()
    return render(request, 'mainapp/index.html', {'categoriess': categories,'itemss': items})

# categories & items are same page which without cotation 
# the other 2 which with "" cotation those working in the html file


def contact(request):
    return render(request, 'mainapp/contact.html')


def signup(request):
    form = SignupForm()
    return render(request, 'mainapp/signup.html')


def signin(request):
    form = SigninForm()
    return render(request, 'mainapp/signin.html')
