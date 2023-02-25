from django.shortcuts import render, redirect
from products.models import Products, Hashtag, Review
from products.forms import ProductCreateForm, ReviewCreateForm



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


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Products.objects.get(id=id)

        context = {
            'product': product,
            'reviews': product.review_set.all(),
            'form': ReviewCreateForm
        }
        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product = Products.objects.get(id=id)
        data = request.POST
        form = ReviewCreateForm(data=data)

        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                rate=form.cleaned_data.get('rate'),
                product=product
            )

        context = {
            'product': product,
            'reviews': product.review_set.all(),
            'form': form
        }

        return render(request, 'products/detail.html', context=context)


def create_product_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES

        form = ProductCreateForm(data, files)

        if form.is_valid():
            Products.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                phone_status=form.cleaned_data.get('phone_status')
            )
            return redirect('/products')

        return render(request, 'products/create.html', context={
            'form': form
        })


