from django.db import models

from django.contrib.auth.models import User



# Create your models here:
class House(models.Model):

    name = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена")
    description = models.TextField("Описание")
    photo = models.ImageField("Фотография", upload_to='houses/photos', default='', blank=True)
    active = models.BooleanField("Активен", default=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"
        ordering = ['-active', 'name']