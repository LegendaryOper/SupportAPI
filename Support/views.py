from rest_framework import viewsets
from rest_framework import permissions
from .models import Ticket, TicketMessage
from .serializers import TicketSerializer, TicketMessageSerializer
from .permissions import IsManager, IsOwner, IsManagerOrAdmin, IsOwnerOrManagerOrAdmin
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


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

    @action(methods=['post', 'get'], permission_classes=[IsOwnerOrManagerOrAdmin], detail=True)
    def messages(self, request, pk=None):
        if self.request.method == 'POST':
            context = {
                "request": self.request,
            }
            request.data._mutable = True
            request.data['ticket'] = self.kwargs['pk']
            request.data._mutable = False
            serializer = TicketMessageSerializer(data=request.data, context=context)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        else:
            queryset = TicketMessage.objects.filter(ticket=self.kwargs['pk']).order_by('created_at')
            serializer = TicketMessageSerializer(queryset, many=True)
            return Response(serializer.data)


# class TicketMessageViewSet(viewsets.ModelViewSet):
#     """A viewset for ticket messages"""
#     serializer_class = TicketMessageSerializer
#
#     def get_queryset(self):
#         print(self.request.data)
#         return TicketMessage.objects.all()













