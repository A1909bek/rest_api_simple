# from django.shortcuts import render 
# from django.http import HttpResponse 
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer 
# from rest_framework.parsers import JSONParser 
# from rest_framework import status 
# from toys.models import Toy 
# from toys.serializers import ToySerializer

# class JSONResponse(HttpResponse):
#     def __init__(self,data,**kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type']='application/json'
#         super(JSONResponse,self).__init__(content,**kwargs)

# @csrf_exempt
# def toy_list(request):
#     if request.method == 'GET':
#         toys = Toy.objects.all()
#         serializer = ToySerializer(toys,many=True)
#         return JSONResponse(serializer.data,status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ToySerializer(data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data,status=status.HTTP_201_CREATED)
#         return JSONResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# @csrf_exempt
# def toy_detail(request,pk):
#     if request.method == 'GET':
#         toy = Toy.objects.get(pk=pk)
#         serializer = ToySerializer(toy)
#         return JSONResponse(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ToySerializer(data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data,status=status.HTTP_200_OK)
#         return JSONResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         toy = Toy.objects.get(pk=pk)
#         toy.delete()
#         return JSONResponse(status=status.HTTP_204_NO_CONTENT)


from django.shortcuts import render 
from rest_framework import status 
from toys.models import Toy 
from toys.serializers import ToySerializer 
from rest_framework.decorators import api_view 
from rest_framework.response import Response

@api_view(['GET','POST'])
def toy_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        serializer = ToySerializer(toys,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = ToySerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def toy_detail(request,pk):
    if request.method == 'GET':
        toy = Toy.objects.get(pk=pk)
        serializer = ToySerializer(toy)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        toy = Toy.objects.get(pk=pk)
        serializer = ToySerializer(toy)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        toy = Toy.objects.get(pk=pk)
        toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    


    
