from rest_framework import serializers

from services.models import Subscription, Plan


class PlanSerializer(serializers.ModelSerializer):
    """Plan model serializer"""
    class Meta:
        model = Plan
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    """Subscription model serializer"""
    plan = PlanSerializer()
    client_name = serializers.CharField(source='client.company_name', max_length=100)
    email = serializers.EmailField(source='client.user.email')

    class Meta:
        model = Subscription
        fields = ('id', 'plan_id', 'client_name', 'email', 'plan')

