from rest_framework import serializers
from .models import Ticket, TicketMessage


class TicketSerializer(serializers.ModelSerializer):
    """ A ticket model serializer"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault(),)

    class Meta:
        model = Ticket
        fields = '__all__'


class TicketMessageSerializer(serializers.ModelSerializer):
    """ A ticket message model serializer"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TicketMessage
        fields = '__all__'

