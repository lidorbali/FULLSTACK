from django.http import JsonResponse
from django.shortcuts import render
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


# get only
def index(request):
    return JsonResponse({'test': "test"})


# desc ,price,prodName,createdTime, _id
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def products(request, id=-100):
    if request.method == 'GET':
        if int(id) > -1:  # get single product
            print(id)
            product = Product.objects.get(_id=id)
            return JsonResponse({
                "desc": product.desc,
                "price": product.price
            }, safe=False)
        else:  # return all
            res = []  # create an empty list
            for productObj in Product.objects.all():  # run on every row in the table...
                res.append(
                    {"desc": productObj.desc,
                     "price": productObj.price,
                     "id": productObj._id
                     }
                )  # append row by to row to res list
            # return array as json response
            return JsonResponse(res, safe=False)

    if request.method == 'POST':  # method post add new row
        # print(request.data['desc'])
        # myDesc =request.data['desc']
        # myPrice=request.data['price']
        Product.objects.create(
            desc=request.data['desc'], price=request.data['price'])
        return JsonResponse({'POST': "success"})

    if request.method == 'DELETE':  # method delete a row
        Product.objects.get(_id=id).delete()
        return JsonResponse({'DELETE': "del"})
    if request.method == 'PUT':  # method put a row
        temp = Product.objects.get(_id=id)
        temp.price = request.data['price']
        temp.desc = request.data['desc']
        temp.save()
        return JsonResponse({'PUT': id})
