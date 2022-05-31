from .models import Ticket, StatusForTicket
from django.shortcuts import get_object_or_404
from .tasks import send_status_mail


def add_to_request_data(request_data, key, value):
    request_data._mutable = True
    request_data[key] = value
    request_data._mutable = False
    return request_data


def get_ticket_user_email(pk):
    ticket = Ticket.objects.get(pk=pk)
    user_email = ticket.user.email
    return user_email


def get_changed_status(request):
    changed_status_id = request.data.get('status', False)
    if changed_status_id is not False:
        changed_status = str(get_object_or_404(StatusForTicket, pk=changed_status_id))
        return changed_status
    return False


def send_email(request, status_id):
    changed_status = get_changed_status(request)
    if changed_status is not False:
        email_to_send = get_ticket_user_email(status_id)
        send_status_mail.delay(changed_status, email_to_send)

