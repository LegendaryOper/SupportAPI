from rest_framework import viewsets
from rest_framework import permissions
from .models import Ticket
from .serializers import TicketSerializer
from .permissions import IsManager, IsOwner, IsManagerOrAdmin, IsOwnerOrManagerOrAdmin
from django.shortcuts import get_object_or_404


class TicketViewSet(viewsets.ModelViewSet):
    """ViewSet for all Ticket objects"""
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    # a method that set permissions depending on http request methods
    def get_permissions(self):
        if self.action in ['update', 'destroy', 'list']:
            self.permission_classes = [IsManagerOrAdmin]
        elif self.action in ['create']:
            self.permission_classes = (permissions.IsAuthenticated,)
        elif self.action in ['partial_update', 'retrieve']:
            self.permission_classes = (IsOwnerOrManagerOrAdmin,)
        else:
            self.permission_classes = (permissions.AllowAny,)
        return super(self.__class__, self).get_permissions()











