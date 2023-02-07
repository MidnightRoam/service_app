import datetime
import time

from celery import shared_task
from celery_singleton import Singleton
from django.conf import settings
from django.core.cache import cache
from django.db import transaction
from django.db.models import F


@shared_task(base=Singleton)
def set_price(subscription_id):
    """
    Celery task which recalculates the subscription
    cost based on the discount percentage and
    the cost of the tariff plan
    """
    from services.models import Subscription

    with transaction.atomic():
        subscription = Subscription.objects.select_for_update().filter(id=subscription_id).annotate(
            anotated_price=F('service__full_price') -
                           F('service__full_price') * F('plan__discount_percent') / 100.00).first()

        subscription.price = subscription.anotated_price
        subscription.save()
    cache.delete(settings.PRICE_CACHE_NAME)


@shared_task(base=Singleton)
def set_comment(subscription_id):
    """
    Celery task which set current time of
    updating/creating in subscription as 'Comment'
    """
    from services.models import Subscription

    with transaction.atomic():
        subscription = Subscription.objects.select_for_update().get(id=subscription_id)

        subscription.comment = str(datetime.datetime.now())
        subscription.save()
    cache.delete(settings.PRICE_CACHE_NAME)
