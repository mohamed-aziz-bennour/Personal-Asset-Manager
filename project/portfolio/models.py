from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
  

# Create your models here.
class Portfolio(models.Model):
    portfolio_name = models.CharField(max_length = 255)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.portfolio_name

    def to_json(self):
        return dict(
            id = self.id,
            portfolio_name = self.portfolio_name
            

        )



class Asset(models.Model):
    portfolio = models.ForeignKey(Portfolio)
    quantity = models.IntegerField()
    cost_basis = models.DecimalField(max_digits = 6, decimal_places = 2)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id') 
