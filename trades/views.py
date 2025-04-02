from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Trade
from .serializers import TradeSerializer

class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['PUT', 'PATCH'])
def produit_detail(request, pk):
    try:
        produit = Trade.objects.get(pk=pk)
    except Trade.DoesNotExist:
        return Response({'error': 'Produit non trouvé'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TradeSerializer(produit, data=request.data)
    elif request.method == 'PATCH':
        serializer = TradeSerializer(produit, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def produit_delete(request, pk):
    try:
        produit = Trade.objects.get(pk=pk)
    except Trade.DoesNotExist:
        return Response({'error': 'Produit non trouvé'}, status=status.HTTP_404_NOT_FOUND)

    produit.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
