from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from store.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('user', UserViewSet)
router.register('product-list', ProductListView, basename='product-list')
router.register('category-list', CategoryListView, basename='category-list')
router.register('specification-product', SpecificationDetail, basename='specification=product')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth', include('djoser.urls')),
    path('api/auth/token', include('djoser.urls.authtoken')),
]
