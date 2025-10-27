from django.db import models

# Create your models here.


class Animals(models.Model):
    CATEGORY_CHOICES = [
        ('predator', 'Predator'),     # Vahshiy, yirtqich dengiz hayvonlari (masalan, akulalar)
        ('herbivore', 'Herbivore'),   # Suv o‘tlari bilan oziqlanadiganlar
        ('omnivore', 'Omnivore'),     # Ham o‘t, ham go‘sht bilan oziqlanadiganlar
        ('other', 'Other'),           # Boshqa turlar
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='animals/')
    category = models.CharField(max_length=255,choices=CATEGORY_CHOICES, default='other')
    habitat = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    lifespan = models.CharField(max_length=255)
    interesting_fact = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

    class Meta:
        ordering = ['category', 'name']
        verbose_name = "Marine Animal"
        verbose_name_plural = "Marine Animals"