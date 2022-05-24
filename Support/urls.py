from .views import TicketViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'ticket', TicketViewSet, basename='ticket')
urlpatterns = router.urls
