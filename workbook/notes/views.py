from rest_framework import mixins, viewsets

from notes.models import UserWord
from notes.serializers import UserWordSerializer


class UserWordViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    model = UserWord
    queryset = UserWord.objects.order_by('-created_at')[:10]
    serializer_class = UserWordSerializer

    authentication_classes = []  # TODO: add csrf token at frontend code
