from django.db import models

# Create your models here:
class House(models.Model):
    name = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена")
    description = models.TextField("Описание")
    photo = models.ImageField("Фотография", upload_to="houses/photos", default="", blank=True)
    
    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"
        ordering = ["name"]
        
    def __str__(self):
        return self.name