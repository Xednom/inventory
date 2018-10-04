from rest_framework import routers
from inventory.views import ItemViewSet


router = routers.DefaultRouter()

router.register(r'item', ItemViewSet)
