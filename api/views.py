from .models import Item
from rest_framework.viewsets import ModelViewSet
from .serializers import ItemSerializer
from rest_framework.generics import CreateAPIView
from api.serializers import UserSerializer
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import AllowAny


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        print(serializer.is_valid())

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
