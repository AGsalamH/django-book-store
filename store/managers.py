from django.db import models
from django.db.models.query import Q


class ProductManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def not_active(self):
        return super().get_queryset().filter(is_active=False)

    def out_of_stock(self):
        return super().get_queryset().filter(in_stock=False)

    def not_available(self):
        return super().get_queryset().filter(Q(is_active=False) | Q(in_stock=False))
