from rest_framework.viewsets import ModelViewSet
from pidatamodel.models import Portfolio
from .serializers import PortfolioSerializer


class PortfolioViewSet(ModelViewSet):
    def get_queryset(self):
        current_user = self.request.user
        return Portfolio.objects.filter(owner=current_user)

    serializer_class = PortfolioSerializer
