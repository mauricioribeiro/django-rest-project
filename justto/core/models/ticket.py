# coding=utf-8
from django.db import models
from django.contrib.postgres.fields import HStoreField

from .user import User
from .audit import *
from . import utils


class TicketStatus:

    OPEN = ('OPEN', 'Aberto')
    DEALING = ('DEALING', 'Em negociação')
    DEAL_SUCCESS = ('DEAL_SUCCESS', 'Negociado com sucesso')
    DEAL_FAIL = ('DEAL_FAIL', 'Não negociado')

    STATUSES = [
        OPEN,
        DEALING,
        DEAL_SUCCESS,
        DEAL_FAIL
    ]

    def __init__(self):
        pass


class Ticket(Audit):
    processNumber = models.CharField(verbose_name='Número do Processo', null=True, blank=True, max_length=25)
    description = models.TextField(verbose_name='Descrição', null=True, blank=True)
    lowerRange = utils.MoneyField(verbose_name='Valor da Alçada Mínima')
    upperRange = utils.MoneyField(verbose_name='Valor da Alçada Máxima')
    dealValue = utils.MoneyField(verbose_name='Valor do Acordo')
    dueDate = models.DateField(verbose_name='Data de Devolução', null=True, blank=True)
    status = models.CharField(choices=TicketStatus.STATUSES, default=TicketStatus.OPEN[0], max_length=25)
    customFields = HStoreField(verbose_name='Campos Customizáveis', blank=True, null=True)
    counterparties = models.ManyToManyField(User, verbose_name='Contrapartes', related_name='ticketsAsCounterpart')
    lawyers = models.ManyToManyField(User, verbose_name='Advogados', related_name='ticketsAsLawyer')
    defendants = models.ManyToManyField(User, verbose_name='Réus', related_name='ticketsAsDefendant')

    class Meta:
        verbose_name = 'Ticket'
        ordering = ['id']

    def __str__(self):
        return self.processNumber

