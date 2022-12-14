from django.urls import path
from rest_framework.routers import SimpleRouter
from api import views
from api.views import ProductViewSet


router = SimpleRouter()

router.register(r'product', ProductViewSet)

urlpatterns = [
    path('product/', ProductViewSet.as_view({'get': 'list'})),
    path('product/<int:id>', views.ProductDetail.as_view()),
]

urlpatterns += router.urls