from django.db import models


class Repositorie(models.Model):
    """ Models of Competition """
    repositorie_id = models.IntegerField('ID')
    name = models.CharField('Nome', max_length=100)
    url = models.CharField('URL', max_length=255)
    language = models.CharField('Linguagem', max_length=20)
    tag = models.CharField('Tags', blank=True, null=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Repositório'
        verbose_name_plural = 'Repositórios'
