from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):

    user_name = models.ForeignKey( User, on_delete = models.CASCADE, default = 1 )
    item_name = models.CharField(max_length=200)
    item_description = models.TextField(max_length=300)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default= "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.ukvisitorguide.cn%2Fwp-content%2Fuploads%2F2015%2F11%2FFood-placeholder.jpg&f=1&nofb=1")

    def __str__(self):
        return f"{self.item_name} {self.item_price}"

    def get_absolute_url(self):
        return reverse( 'food:detail',kwargs = { "pk" : self.pk  } )

        