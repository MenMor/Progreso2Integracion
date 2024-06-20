from django.shortcuts import render, redirect
from .models import Product, Order
import requests

def get_product_image(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}')
    if response.status_code == 200:
        data = response.json()
        return data['sprites']['front_default']
    return None

def create_order(request):
    product_id = request.GET.get('product_id') or request.POST.get('product_id')
    if not product_id:
        return render(request, 'create_order.html', {'error': 'No product ID provided'})
    
    if request.method == 'POST':
        product_id = request.POST['product_id']
        quantity = request.POST['quantity']
        customer_name = request.POST['customer_name']
        customer_email = request.POST['customer_email']

        try:
            product = Product.objects.get(id=product_id)
            Order.objects.create(product=product, quantity=quantity, customer_name=customer_name, customer_email=customer_email)
            return render(request, 'order_success.html')
        except Product.DoesNotExist:
            return render(request, 'create_order.html', {'error': 'Product not found', 'product_id': product_id})
        except ValueError:
            return render(request, 'create_order.html', {'error': 'Invalid product ID', 'product_id': product_id})
    
    context = {'product_id': product_id}
    return render(request, 'create_order.html', context)

def list_products(request):
    products = Product.objects.all()
    products_with_images = []
    for product in products:
        image_url = get_product_image(product.name)
        products_with_images.append({
            'name': product.name,
            'stock': product.stock,
            'image_url': image_url
        })
    return render(request, 'list_products.html', {'products': products_with_images})
