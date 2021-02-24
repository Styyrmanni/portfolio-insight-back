from rest_framework.serializers import ModelSerializer
from pidatamodel.models import Portfolio
from django.conf import settings


class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['name', 'owner', 'created', 'modified']
