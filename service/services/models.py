from django.core.validators import MaxValueValidator
from django.db import models

from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=100)
    full_price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Plan(models.Model):
    class PlanTypes(models.TextChoices):
        full = 'Full'
        student = 'Student'
        discount = 'Discount'

    plan_type = models.CharField(max_length=10, choices=PlanTypes.choices)
    discount_percent = models.PositiveIntegerField(default=0,
                                                   validators=[
                                                       MaxValueValidator(100),
                                                   ])

    def __str__(self):
        return f'Plan: {self.plan_type} ({self.discount_percent}%)'


class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscriptions', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='subscriptions', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscriptions', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.client} | Service: {self.service} | {self.plan}'
