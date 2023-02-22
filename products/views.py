from django.shortcuts import render
from products.models import Products, Hashtag

def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def products_view(request):
    if request.method == 'GET':
        products = Products.objects.all()

        context = {
            'products': [
                {
                    'id': product.id,
                    'title': product.title,
                    'image': product.image,
                    'phone_status': product.phone_status,
                    'hashtags': product.hashtags.all()
                } for product in products
            ]
        }
        return render(request, 'products/products.html', context=context)

def hashtags_view(request):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        context = {
            'hashtags': hashtags
        }
        return render(request, 'products/hashtags.html', context=context)
