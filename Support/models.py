from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class StatusForTicket(models.Model):
    """Status model for Ticket"""

    TICKET_STATUS_CHOICES = [
        ('open', 'open'),
        ('in process', 'in process'),
        ('closed', 'closed')
    ]
    name = models.CharField(verbose_name='name', max_length=30, choices=TICKET_STATUS_CHOICES)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    """A Ticket model"""
    header = models.CharField(verbose_name='header', max_length=30)
    description = models.CharField(verbose_name='description', max_length=500)
    status = models.ForeignKey(StatusForTicket, verbose_name='status', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)


class TicketMessage(models.Model):
    """A message for ticket model"""
    message = models.CharField(verbose_name='description', max_length=500)
    ticket = models.ForeignKey(Ticket, verbose_name='ticket', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
