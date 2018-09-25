# coding=utf-8
from django.db import models


class Audit(models.Model):
    createdBy = models.EmailField(verbose_name='Criado por', default='system@justto.com')
    createdAt = models.DateField(verbose_name='Criado em', auto_now_add=True)
    updatedBy = models.EmailField(verbose_name='Atualizado por', default='system@justto.com')
    updatedAt = models.DateField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        abstract = True

    @staticmethod
    def fields():
        return 'createdBy', 'createdAt', 'updatedBy', 'updatedAt'
