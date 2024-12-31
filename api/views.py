from .models import Item
from rest_framework.viewsets import ModelViewSet
from .serializers import ItemSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
