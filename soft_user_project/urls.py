from rest_framework import routers
from .api import SoftUserProjectViewSet

router = routers.DefaultRouter()

router.register('api/soft_user_project', SoftUserProjectViewSet, 'soft_user_project' )
urlpatterns = router.urls

