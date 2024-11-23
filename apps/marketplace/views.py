from django.shortcuts import render

def about_view(request):
    return render(request, 'about.html')

def farmer_dashboard(request):
    return render(request, 'farmer_dashboard.html')

def supplier_dashboard(request):
    return render(request, 'supplier_dashboard.html')
