from celery import shared_task
from celery_singleton import Singleton
from django.db.models import F


@shared_task(base=Singleton)
def set_price(subscription_id):
    from services.models import Subscription

    subscription = Subscription.objects.filter(id=subscription_id).annotate(
        anotated_price=F('service__full_price') -
                       F('service__full_price') * F('plan__discount_percent') / 100.00).first()

    subscription.price = subscription.anotated_price
    subscription.save()
