from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import ProductReview, ShopReview
from .serializers import ProductReviewSerializer, ShopReviewSerializer

class ProductReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ProductReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return ProductReview.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ShopReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ShopReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return ShopReview.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)