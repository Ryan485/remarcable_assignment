# Author: Ryan Song

from django.shortcuts import render
from .models import Product, Category, Tag


def product_list(request):
    """
    Display a list of products with optional search and filter functionality.
    :param request: HTTP request object containing search and filter parameters
    :precondition: request must be a valid HTTP GET request
    :postcondition: returns filtered products based on search/category/tag inputs
    :return: rendered HTML template with filtered products, categories and tags
    """
    
    # fetch all products, tags, and categories from the database to populate the dropdowns
    products = Product.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    search = request.GET.get('search')
    category = request.GET.get('category')
    tag = request.GET.get('tags')

    if search:
        products = products.filter(description__contains = search)

    if category:
        products = products.filter(category__id = category)

    if tag:
        products = products.filter(tags__id = tag)

    return render(request, 'index.html', {
        'products' : products,
        'categories' : categories,
        'tags' : tags
        })