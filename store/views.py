from django.shortcuts import render

# Create your views here.
from store.models import Category, Products


#
# def store(request):
#     context = {}
#     return render(request, 'store/store.html', context)

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()

    data = {'products': products, 'categories': categories}

    # print('you are : ', request.session.get('email'))
    return render(request, 'store/store.html', data)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
