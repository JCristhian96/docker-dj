from rest_framework import routers, urlpatterns
# ViewSets
from apps.core.api import viewsets

router = routers.SimpleRouter()

router.register('persons', viewsets.PersonViewSet, basename="persons")

urlpatterns = router.urls