from django.shortcuts import render
from .forms import CustomerModelForm
from .models import Customer
def details(request):
    if request.method == 'POST':
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            all_customers = Customer.objects.all().order_by('name')
            filtered_customers = Customer.objects.filter(email__endswith='@example.com')
            return render(request,'form-data.html',{
                'message': 'Customer Info Stored',
                'all_customers': all_customers,
                'filtered_customers': filtered_customers
            })
    else:
        form = CustomerModelForm()
    return render(request,'index.html',{'form':form})