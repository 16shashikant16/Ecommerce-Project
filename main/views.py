from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product, Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')





def product_list(request):
    # Fetch all products from the database
    products = Product.objects.all()
    
    # Render the 'product_list.html' template with the products context
    return render(request, 'main/product_list.html', {'products': products})



def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # Save the product to the database
            return redirect('/products/')  # Redirect to product list after creation
    else:
        form = ProductForm()  # Provide an empty form for GET request
    
    return render(request, 'create_product.html', {'form': form})



def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/products/')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})




# def place_order(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     if request.method == 'POST':
#         customer_name = request.POST['customer_name']
#         address = request.POST['address']
#         Order.objects.create(product=product, customer_name=customer_name, address=address)
#         return redirect('order_success')
#     return render(request, 'main/place_order.html', {'product': product})



from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

@login_required
def order_placement(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            total_price = product.price * quantity  # Calculate total price
            order = form.save(commit=False)
            order.user = request.user  # Associate the order with the current user
            order.product = product  # Associate the product with the order
            order.total_price = total_price
            order.save()  # Save the order to the database
            return redirect('order_success')  # Redirect to order success page
    else:
        form = OrderForm()

    return render(request, 'main/order_placement.html', {'form': form, 'product': product})



####





def order_success(request):
    return render(request, 'main/order_success.html')










def home_view(request):
    return render(request, 'main/home.html')  # Render a home page template


