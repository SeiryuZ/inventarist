from django.conf import settings
from django.db import models


class Log(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='logs')
    product = models.ForeignKey('products.Product', blank=True, null=True, related_name='logs')

    ACTION_CHOICES = (
        ('1', 'Add product'),
        ('2', 'Edit Product'),
        ('3', 'Remove Product'),
    )
    action = models.PositiveIntegerField(choices=ACTION_CHOICES)

    def __unicode__(self):
        if self.product:
            return " #%s" % (self.product_id,)
        else:
            return self.action
