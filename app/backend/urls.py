from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import SimpleRouter
from user.views import UserViewSet, LoginViewSet, RefreshViewSet, RegistrationViewSet
from store.views import ItemViewSet, OrderViewSet, CategoryViewSet, checkout, health_check
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)

routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register(r'user', UserViewSet, basename='user')

# api
routes.register(r'item', ItemViewSet, basename='item')
routes.register(r'category', CategoryViewSet, basename='category')
routes.register(r'order', OrderViewSet, basename='order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routes.urls)),
    path('api/checkout/', checkout, name='checkout'),
    path('api/health-check/', health_check, name='health-check'),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
