# coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.contrib.postgres.fields import HStoreField

from .audit import *


class UserPerson:
    NATURAL = ('NATURAL', 'Pessoa Física')
    LEGAL = ('LEGAL', 'Pessoa Jurídica')

    TYPES = [NATURAL, LEGAL]

    def __init__(self):
        pass


class User(AbstractBaseUser, Audit):
    person = models.CharField(verbose_name='Pessoa', choices=UserPerson.TYPES, default=UserPerson.NATURAL[0], max_length=10)
    name = models.CharField(verbose_name='Nome', max_length=100)
    legalId = models.CharField(verbose_name='Documento', unique=True, max_length=25)
    username = models.CharField(verbose_name='Usuario', unique=True, max_length=25)
    is_admin = models.BooleanField(default=False)
    customFields = HStoreField(verbose_name='Campos Customizaveis', blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    class Meta:
        verbose_name = 'Usuário'
        ordering = ['username']

    def __str__(self):
        return self.username

