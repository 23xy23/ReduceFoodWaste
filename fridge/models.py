from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="food_images/", blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(default=1)
    expiry_date = models.DateField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
