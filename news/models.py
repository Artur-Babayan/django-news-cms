from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField(Category, related_name='news')
    main_category = models.ForeignKey(Category, related_name='main_news', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
