from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ItemViewSet, RegisterView

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

custom_patterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register')
]

urlpatterns = router.urls + custom_patterns
