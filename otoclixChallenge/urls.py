from .viewsets import PostViewset
from rest_framework.routers import SimpleRouter

class CustomRouter(SimpleRouter):
    def __init__(self):
        super().__init__()
        self.trailing_slash = '/?'

router = CustomRouter()
router.register(r'posts', PostViewset, basename='posts')
urlpatterns = router.urls