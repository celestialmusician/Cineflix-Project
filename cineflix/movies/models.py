from django.db import models

# Create your models here.

import uuid

from multiselectfield import MultiSelectField

from embed_video.fields import EmbedVideoField

class BaseClass(models.Model):

    uuid=models.UUIDField(unique=True,default=uuid.uuid4)

    active_status=models.BooleanField(default=True)

    created_at= models.DateField(auto_now_add=True)

    updated_at=models.DateField(auto_now=True)

    class Meta:

        abstract=True


class IndusttryChoices(models.TextChoices):

    MOLLYWOOD='Mollywood','Mollywod'
    
    HOLLYWOOD='Hollywood','Hollywod'

    BOLLYWOOD='Bollywood','Bollywod'

    TOLLYWOOD='Tollywood','Tollywod'

class CertificateChoices(models.TextChoices):

    A='A','A'

    UA='UA','UA'

    U='U','U'

    S='S','S'

class GenereChoices(models.TextChoices):

    ACTION='Action','Acton'

    ROMANTIC='Romantic','Romantic'

    THRILLER='Thriller','Thriller'

    HORROR='Horror','Horror'

class ArtistChoices(models.TextChoices):

    MOHANLAL='Mohan Lal','Mohan Lal'

    MAMMMOOTTY='Mammootty','Mammootty'

    NIVINPAULY='Nivin Pauly','Nivin Pauly'

class LanguagesChoices(models.TextChoices):

    MALAYALAM='Malayalam','Malayalam'

    ENGLISH='English','English'

    HINDI='Hindi','Hindi'

    TAMIL='Tamil','Tamil'

    TELUGU='Telegu','Telugu'

    KANNADA='Kannada','Kannada'


class Movie(BaseClass):

    name=models.CharField(max_length=50)

    description=models.TextField

    release_year=models.DateField()

    industry= models.CharField(max_length=20,choices=IndusttryChoices.choices)

    runtime=models.TimeField()

    certification=models.CharField(max_length=5,choices=CertificateChoices.choices)

    genre=MultiSelectField(max_length=30,choices=GenereChoices.choices)

    artists=MultiSelectField(max_length=30,choices=ArtistChoices.choices)

    video=EmbedVideoField()

    tags=models.TextField()

    languages=MultiSelectField(max_length=50,choices=LanguagesChoices.choices)

    class Meta:

        verbose_name='Movies'

        verbose_name_plural='Movies'

    def __str__(self):

        return f'{self.name}'

