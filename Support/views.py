from rest_framework import viewsets
from rest_framework import permissions
from .models import Ticket, TicketMessage
from .serializers import TicketSerializer, TicketMessageSerializer
from .permissions import IsManager, IsOwner, IsManagerOrAdmin, IsOwnerOrManagerOrAdmin
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .services import add_to_request_data


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
        elif self.action in ['partial_update', 'retrieve', 'messages']:
            self.permission_classes = (IsOwnerOrManagerOrAdmin,)
        else:
            print(self.action)
            self.permission_classes = (permissions.AllowAny,)
        return super(self.__class__, self).get_permissions()

    @action(methods=['post', 'get'], detail=True)
    def messages(self, request, pk=None):
        self.check_permissions(request)
        self.check_object_permissions(request, self.get_object())
        if self.request.method == 'POST':
            context = {
                "request": self.request,
            }
            changed_request_data = add_to_request_data(request.data, 'ticket', self.kwargs['pk'])
            serializer = TicketMessageSerializer(data=changed_request_data, context=context)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        else:
            queryset = TicketMessage.objects.filter(ticket=self.kwargs['pk']).order_by('created_at')
            serializer = TicketMessageSerializer(queryset, many=True)
            return Response(serializer.data)
















