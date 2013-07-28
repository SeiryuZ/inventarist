from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    quantity = models.PositiveIntegerField()
    limit = models.PositiveIntegerField()

    def __unicode__(self):
        return "#%s | %s" % (self.id, self.name)
