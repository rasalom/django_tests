from django.conf import settings
from django.db import models
from core.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager


class Category(TimeStampedModel, MPTTModel):
    """
    Category model
    """
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
                            on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = TaggableManager()

    class Meta:
        unique_together = ('parent', 'slug')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Ranking(TimeStampedModel):
    """
    Ranking model
    """
    title = models.CharField(max_length=255, blank=False, null=False, unique=True)
    subtitle = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    slug = models.SlugField()
    category = TreeForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class Product(TimeStampedModel):
    """
    Product model
    """
    title = models.CharField(max_length=255, blank=False, null=False, unique=True)
    subtitle = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField()
    tags = TaggableManager()
    ranking = models.ManyToManyField(Ranking)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
