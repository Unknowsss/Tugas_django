from django.shortcuts import render
from subscribe.models import Customer
from subscribe.forms import NewSubscriber
# Create your views here.
def index(request):
    return render(request, 'subscribe/index.html')

def customers(request):
    customers_list = Customer.objects.order_by('first_name')
    customers_dict = {'customers':customers_list}
    return render(request, 'subscribe/customers.html', context=customers_dict)

def subscribe(request):
    form = NewSubscriber()

    if request.method == "POST" :
        form = NewSubscriber(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return customers(request)
        else:
            print("error : form invalid")

    return render (request, 'subscribe/subscribe.html', {'form' :form})