from django.db import models

# Create your models here:
class House(models.Model):

    name = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")
    price = models.IntegerField("Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"
        ordering = ['name']