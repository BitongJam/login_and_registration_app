from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializers
from rest_framework import status
from django.shortcuts import get_object_or_404

# @api_view(['GET'])
# def getData(request):
#     items = Item.objects.all()
#     serializer = ItemSerializers(items,many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def getData(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = Item.objects.filter(**request.query_params.dict())
    else:
        items = Item.objects.all()
    serializer = ItemSerializers(items,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()

@api_view(['POST'])
def updateItem(request,pk):
    item = Item.objects.get(pk=pk)
    data = ItemSerializers(instance=item,data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
 
@api_view(['DELETE'])
def deleteItem(request,pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)