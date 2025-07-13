from django.shortcuts import render
from .models import Product
from datetime import datetime

# Create your views here.
def logger(message=""):
    log_file = open("./order_builder.log", "a")
    log_message = f"{message} at {datetime.now()}\n"
    log_file.writelines(log_message)
    log_file.close()

def show_products(request):
    product_list = Product.objects.all()
    item_name = request.GET.get('item_name')
    logger(item_name)
    if item_name != "" and item_name is not None:
        product_list = product_list.filter(title__icontains=item_name)
    context = {"product_list": product_list}
    return render(request,"shop/index.html", context= context)