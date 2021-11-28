from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .models import *

from store.serializers import *


class LogoutViewSet(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user_data = request.data
        user = User.objects.create(
            username=user_data['username'],
            password=user_data['password'],
            email=user_data['email'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
        )
        Customer.objects.create(user=user)

        token = Token.objects.create(user=user)
        print(token)

        answer = UserSerializer(user).data
        answer['token'] = token.key

        return Response(data=answer, status=status.HTTP_201_CREATED)


class ProductListView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAdminUser | permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAdminUser | permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SpecificationDetail(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated | permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = SpecificationsProduct.objects.all()
    serializer_class = SpecificationProductSerializer

    def get(self, request, *args, **kwargs):

        product = SpecificationsProduct.objects.get(product=request['product'])
        return Response(data=SpecificationProductSerializer(data=product), status=status.HTTP_200_OK)


def index(request):
    return render(request, 'index.html')