from django.shortcuts import render, redirect
from phones.models import Phone


def forming(phones_objects):
    phones = []
    for phone in phones_objects:
        phone_dict = {
            'name': phone.name,
            'price': phone.price,
            'image': phone.image,
            'release_date': phone.release_date,
            'lte_exists': phone.lte_exists,
            'slug': phone.slug
        }
        phones.append(phone_dict)
    return phones


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones_objects = Phone.objects.all()
    if sort == None:
        phones = forming(phones_objects)
    elif sort == 'name':
        phones = sorted(forming(phones_objects), key=lambda phone: phone['name'])
    elif sort == 'min_price':
        phones = sorted(forming(phones_objects), key=lambda phone: phone['price'])
    elif sort == 'max_price':
        phones = sorted(forming(phones_objects), key=lambda phone: phone['price'], reverse=True)
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones_objects = Phone.objects.filter(slug=slug)
    context = {
        'phone': forming(phones_objects)[0]
    }
    return render(request, template, context)