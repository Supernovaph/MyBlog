from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import Product, Order


def homepage(req):
    if req.user.is_authenticated:
        name = req.user.username
    else:
        name = 'Anonymous'
    return render(req, 'homepage.html', {'products':Product.objects.all(), 'username':name})

def is_moderators(user):
    return user.groups.filter(name='Moderators').exists()           

@login_required
@user_passes_test(is_moderators)
def admin_panel(req):
    return render(req, 'adminka.html')

@login_required
@user_passes_test(is_moderators)
def create_product(req):
    try:
        Product.objects.create(
            name=req.POST['title'],
            description=req.POST['description'],
            price=req.POST['price'],
            amount=req.POST['amount'],
            image=req.POST['image'])
    except Exception as e:
        return HttpResponseBadRequest(e)
    return HttpResponseRedirect('adminka')

@login_required
def add_product(req):
    a = get_object_or_404(Product, pk = req.POST['id'])
    orders = list(Order.objects.filter(user=req.user))
    if orders:
        order = orders[0] 
    else:
        order = Order(user=req.user)
        order.save()
    
    
    order.tovars.add(a)
    order.save()
    return HttpResponse('Cool')

def reg(req):
    if 'login' in req.POST and 'password' in req.POST:
        try:
            user = User.objects.create_user(req.POST['login'], password = req.POST['password'])
            return HttpResponseRedirect('home')
        except:
            return HttpResponseBadRequest()
    else:        
        return render(req, "register.html")

@login_required
def viewcart(req):
    a = Order.objects.get(user=req.user)
    tovars = a.tovars.all()
    print(tovars)
    return render(req, "viewcart.html",{'item':tovars})


 


