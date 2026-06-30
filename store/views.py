from .models import Order, OrderItem
from .models import Product, Category
from django.shortcuts import redirect
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

def home(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')
    products = Product.objects.all()
    if query:
        products = products.filter(
            name__icontains=query
        )
    if category_id:
        products = products.filter(
            category_id=category_id
        )
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'products': products,
        'query': query,
        'categories': categories,
        'selected_category': category_id,
    })  


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {
        'product': product
    })

@login_required
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    request.session['cart'] = cart
    return redirect('home')

def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        request.session['checkout_data'] = {
            'name': name,
            'email': email,
            'address': address,
        }
        return redirect('payment')
    return render(request, 'store/checkout.html')

def order_success(request):
    return render(request, 'store/order_success.html')
    
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(username=email).exists():
                form.add_error('email', 'This email is already registered.')
            else:
                user = form.save(commit=False)
                user.username = email
                user.email = email
                user.save()
                return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'store/register.html', {
        'form': form
    })
    

@login_required
def my_orders(request):
    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')
    return render(
        request,
        'store/my_orders.html',
        {
            'orders': orders
        }
    )

@login_required
def payment(request):
    if request.method == 'POST':
        checkout_data = request.session.get('checkout_data')
        cart = request.session.get('cart', {})
        order = Order.objects.create(
            user=request.user,
            customer_name=checkout_data['name'],
            email=checkout_data['email'],
            address=checkout_data['address']
        )
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )
        request.session['cart'] = {}
        request.session.pop('checkout_data', None)
        return redirect('order_success')
    return render(request, 'store/payment.html')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    if product_id in cart:
        del cart[product_id]
    request.session['cart'] = cart
    if len(cart) == 0:
        return redirect('home')
    return redirect('cart')

def increase_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    if product_id in cart:
        cart[product_id] += 1
    request.session['cart'] = cart
    return redirect('cart')
    
def decrease_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    if product_id in cart:
        cart[product_id] -= 1
        if cart[product_id] <= 0:
            del cart[product_id]
    request.session['cart'] = cart
    return redirect('cart')

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    total_orders = Order.objects.filter(
        user=request.user
    ).count()
    return render(
        request,
        'store/profile.html',
        {
            'total_orders': total_orders
        }
    )
