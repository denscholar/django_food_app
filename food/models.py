from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.ImageField(upload_to='media', default='media/default.jpg')

    def __str__(self):
        return self.item_name
    


