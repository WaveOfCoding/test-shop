from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from api.models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['status']
    search_fields = ['sku', 'title']

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetail(APIView):
    def get(self, request, id):
        try:
            queryset = Product.objects.get(id=id)

        except Product.DoesNotExists:
            msg = {'msg': 'Not Found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

