from django.shortcuts import render

def buyer_home(request):
    products = [
        {
            'name': 'Tomatoes',
            'img': 'https://www.garden-products.co.uk/wp-content/uploads/2024/02/Tomatoes-scaled.jpeg',
            'price': 2.50,
            'description': 'Fresh tomatoes from the farm',
            'quantity': 100
        },
        {
            'name': 'Cucumbers',
            'img': 'https://cdn.jwplayer.com/v2/media/oioYxJP7/poster.jpg?width=720',
            'price': 1.50,
            'description': 'Fresh cucumbers from the farm',
            'quantity': 50
        },
        {
            'name': 'Potatoes',
            'img': 'https://phs-prod.s3.us-east-1.amazonaws.com/attachments/cl2z2ike3hqpd9zra4f5ltvre-potatoes-g142c78d3f-1920.12.0.1894.1263.full.jpg',
            'price': 3.00,
            'description': 'Fresh potatoes from the farm',
            'quantity': 75
        },
        {
            'name': 'Carrots',
            'img': 'https://scitechdaily.com/images/Orange-Carrots-Art-Concept.jpg',
            'price': 2.00,
            'description': 'Fresh carrots from the farm',
            'quantity': 100
        }
    ]

    context = {
        'products': products
    }
    return render(request, 'buyers_templates/buyers_base.html', context)