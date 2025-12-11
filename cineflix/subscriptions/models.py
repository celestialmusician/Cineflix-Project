from django.db import models

from multiselectfield import MultiSelectField

# Create your models here.

from movies.models import BaseClass

class DeviceChoices(models.TextChoices) :

    PHONE = 'Phone','Phone'

    TABLET = 'Tablet','Tablet'

    TV = 'TV','TV'

    LAPTOP = 'Laptop','Laptop'

class QualityChoices(models.TextChoices) :

    P480 = '480 p','480 p'

    P1080 = 'Upto 1080 p','Upto 1080 p'

    P4K = 'Upto 4K','Upto 4K'

class ScreenOrDownloadDeviceChoices(models.IntegerChoices) :

    ONE = 1,'1'

    TWO = 2,'2'

    FOUR = 4,'4'


class SubscriptionPlans(BaseClass):

    name = models.CharField(max_length=25)

    amount = models.FloatField()

    devices = MultiSelectField(choices=DeviceChoices.choices)

    quality = models.CharField(max_length=30,choices=QualityChoices.choices)

    no_of_screens = models.IntegerField(choices=ScreenOrDownloadDeviceChoices.choices)

    download_services = models.IntegerField(choices=ScreenOrDownloadDeviceChoices.choices)

    class Meta:


        verbose_name = 'Subscription Plan'

        verbose_name_plural = 'Subscription Plans'
        

    def __str__(self):

        return self.name