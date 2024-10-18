from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import  authenticate, logout, login
from django.contrib import messages
from .models import Products
from django.contrib.auth.decorators import  login_required



User = get_user_model()


def login_page(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            toggle = User.objects.get(username = user)
            if toggle.is_vendor:
                return redirect('dashboard')
            else:
                return redirect('home')
    return render(request, 'auth/login.html')

def signup(request):
    if request.method == 'POST':
        fullname = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        is_vendor = request.POST['customer']
        if is_vendor == 'vendor':
            is_vendor = True
        else:
            is_vendor = False
        try:
            user = User.objects.create_user(first_name=fullname, username=email, email=email, password=password, is_vendor = is_vendor)
            user.save()
            if user:
                return redirect('login')
        except Exception as e:
            print(e)

    return render(request, 'auth/signup.html')

def home(request):
    mobiles = Products.objects.filter(category= 1)
    laptops = Products.objects.filter(category = 2)
    products = Products.objects.all()
    context ={
        'all' : products,
        'mobiles':mobiles,
        'laptops':laptops        
    }
    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def dash(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_desc = request.POST.get('product_desc')
        product_image = request.FILES.get('product_image')
        product_catagory = request.POST.get('catagory')
        user_id = request.user
        print(user_id)

        if product_name and product_price and product_desc and product_image:
            try:
                product_price = float(product_price)
                if product_price <= 0:
                    raise ValueError
            except ValueError:
                messages.error(request, 'Invalid price. It must be a positive number.')
                return render(request, 'add_items.html')

            product = Products(
                name=product_name, 
                price=product_price, 
                description=product_desc, 
                image=product_image,
                user = user_id
            )
            product.save()
            messages.success(request, 'Product added successfully!')
            return redirect('dashboard')
    return render(request, 'add_items.html')


def list_items(request):
    products = Products.objects.filter(user = request.user, )
    context = {
        'products':products
    }
    return render(request, 'items_list.html', context)


def delete_item(request):
    product_id = request.GET.get('product_id')
    product = Products.objects.get(id=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('dashboard')

def shop(request):
    return render(request, 'shop.html')