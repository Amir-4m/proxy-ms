from rest_framework import viewsets, mixins
from apps.services.api.authentications import ServiceAuthentication
from apps.services.api.permissions import ServicePermission

from .serializers import ProxySerializer
from ..models import Proxy


class ProxyViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    authentication_classes = (ServiceAuthentication,)
    permission_classes = (ServicePermission,)
    queryset = Proxy.objects.filter(is_enable=True)
    serializer_class = ProxySerializer
