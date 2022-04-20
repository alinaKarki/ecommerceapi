from django.urls import include, path

app_name = "api_v1"

urlpatterns = [path("product/", include("product.api.v1.urls", namespace="product"))]
