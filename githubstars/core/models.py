from django.db import models


class Repositorie(models.Model):
    """ Models of Competition """
    repositorie_id = models.IntegerField('ID')
    repositorie_name = models.CharField('Nome', max_length=100)
    repositorie_url = models.CharField('URL', max_length=255)
    repositorie_language = models.CharField('Linguagem', max_length=20)
    repositorie_tag = models.CharField('Tags', blank=True, null=True, max_length=255)

    def __str__(self):
        return self.repositorie_name

    class Meta:
        verbose_name = 'Repositório'
        verbose_name_plural = 'Repositórios'
