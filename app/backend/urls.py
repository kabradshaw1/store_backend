from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from user.views import UserViewSet, LoginViewSet, RefreshViewSet, RegistrationViewSet
from store.views import ItemViewSet, OrderViewSet, CategoryViewSet, checkout

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
# routes.register(r'checkout', CheckOutViewSet, basename='checkout') CheckOutViewSet,

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routes.urls)),
    path('api/checkout/', checkout, name='checkout')
]
