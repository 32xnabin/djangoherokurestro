from django.db import models

class Agro(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 255, verbose_name = u'Title')
    addedBy = models.CharField(max_length = 255, verbose_name = u'Added by')
    nextParty = models.CharField(max_length = 255, verbose_name = u'Logo')
    transType = models.CharField(max_length = 255, verbose_name = u'Type')
    category = models.CharField(max_length = 255, verbose_name = u'category')
    amount = models.FloatField(verbose_name = u'Amount')

class Meta:
        ordering = ('created',)