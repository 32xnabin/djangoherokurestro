from django.db import models

class Restro(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length = 255, verbose_name = u'Name')
    email = models.CharField(max_length = 255, verbose_name = u'Email')
    logo = models.CharField(max_length = 255, verbose_name = u'Logo')
    phone = models.CharField(max_length = 255, verbose_name = u'Phone')
    rating = models.IntegerField(verbose_name = u'Rating')

class Meta:
        ordering = ('created',)
