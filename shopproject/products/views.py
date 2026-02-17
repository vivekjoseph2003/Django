from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
from io import BytesIO
from .models import Product
from django.core.mail import send_mail
from django.utils.html import strip_tags

# Home page
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

# Add Product
def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        Product.objects.create(name=name, description=description, price=price)
        return redirect('home')
    return render(request, 'add_product.html')

# Product Detail
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

# PDF Generation
def generate_pdf(request, pk):
    product = get_object_or_404(Product, pk=pk)
    template = get_template('product_pdf.html')
    html = template.render({'product': product})

    buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=buffer)

    if pisa_status.err:
        return HttpResponse('PDF creation error!')
    else:
        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{product.name}.pdf"'
        return response

# Send Email
def send_product_email(request, pk):
    product = get_object_or_404(Product, pk=pk)

    subject = f"New Product: {product.name}"
    from_email = "user123@gmail.com"
    recipient_list = ["your_mailtrap_inbox@mailtrap.io"]

    html_message = render_to_string('product_pdf.html', {'product': product})
    plain_message = strip_tags(html_message)

    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
    return HttpResponse('Email sent successfully')

# Update Product
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.save()
        return redirect('home')
    return render(request, 'add_product.html', {'product': product})

# Delete Product
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('home')
