from django.db.models.signals import pre_save, pre_delete, post_delete, post_save
from django.dispatch import receiver
from cars.models import Car


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    ...


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    ...