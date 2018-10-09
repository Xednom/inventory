from rest_framework import routers
from inventory.views import ItemViewSet, CategoryViewSet


router = routers.DefaultRouter()

router.register(r'item', ItemViewSet)
router.register(r'category', CategoryViewSet)
