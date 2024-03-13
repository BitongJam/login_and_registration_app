from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializers

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