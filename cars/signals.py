from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum

#Função que Atualizar Inventario
def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = 'Nenhuma informação disponível ainda'



@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    #instance = kwargs.get('instance')
    print('### PRE SAVE ###')


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    #instance = kwargs.get('instance')
    print('### POST SAVE ###')
    car_inventory_update()


@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    #instance = kwargs.get('instance')
    print('### PRE DELETE ###')


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    #instance = kwargs.get('instance')
    print('### POST DELETE ###')
    car_inventory_update()

