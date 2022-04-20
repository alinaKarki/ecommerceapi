from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSets, ProductView

app_name = "users_api_v1"

router = DefaultRouter()
router.register(r"category", CategoryViewSets)
# router.register(r"product",ProductView)


urlpatterns = [
    #  path("category/", CategoryView.as_view(), name="category"),
    path("product/", ProductView.as_view(), name="product"),
]

urlpatterns += router.urls
