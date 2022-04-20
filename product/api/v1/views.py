from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from product.models import CategoryModel, ProductModel

from .serializers import CategorySerializer, ProductSerializer

# Create your views here.


class CategoryViewSets(viewsets.ModelViewSet):

    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    # def list(self, request):
    #     context = {}
    #     queryset = CategoryModel.objects.all()
    #     #if list of queryset then many=True arguments is passed
    #     serializer = CategorySerializer(products, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = CategorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):

    def get(self, request, format=None):
        # format is not required
        products = ProductModel.objects.all()
        # if list of queryset then many=True arguments is passed
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
