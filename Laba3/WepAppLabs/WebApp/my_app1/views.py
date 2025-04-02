from .minio import add_pic
from datetime import datetime
from .forms import SendTextForm
from rest_framework import status
from .models import Product, Application
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404


def GetOrders(request):
    elements = Product.objects.filter(deleted_at=None).values()
    return render(request, 'order_element.html', {"data": elements})


def GetOrder(request, id):
    order = Product.objects.filter(id=id).values()
    return render(request, 'order.html', {'data': order})


def order_ok(request, id):
    if request.method == "POST":
        form = SendTextForm(request.POST)
        if form.is_valid():
            quantity = int(form.cleaned_data['text'])
            
            product = get_object_or_404(Product, id=id)

            new_application = Application(is_active=True,
                                          id_product=product,
                                          quantity_product=quantity)
            new_application.save()
            return HttpResponseRedirect(f"/order_ok/{id}/")
        else:
            form = SendTextForm()
    
    return render(request, "order_ok.html")


class ProductList(APIView):
    model_class = Product
    serializer_class = ProductSerializer

    def get(self, requset, format=None):
        products = self.model_class.objects.all()
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            pic = request.FILES.get('pic')
            pic_result = add_pic(product, pic)
            if 'error' in pic_result.data:
                return pic_result
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    model_class = Product
    serializer_class = ProductSerializer

    def get(self, request, pk, format=None):
        product = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(product)
        return Response(serializer.data)
    

    def post(self, request, pk, format=None):
        product = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        product = get_object_or_404(self.model_class, pk=pk)
        product.deleted_at = datetime.now()
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk, format=None):
        product = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(product, data=request.data, partial=True)
        if 'pic' in serializer.initial_data:
            pic_result = add_pic(product, serializer.initial_data['pic'])
            if 'error' in pic_result.data:
                return pic_result
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
