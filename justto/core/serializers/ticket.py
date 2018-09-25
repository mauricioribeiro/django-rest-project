
from rest_framework import serializers

from ..models.ticket import *
from ..models.audit import *


class TicketSerializer(serializers.ModelSerializer):
    customFields = serializers.HStoreField()

    class Meta:
        model = Ticket
        fields = (
            'id',
            'processNumber',
            'description',
            'lowerRange',
            'upperRange',
            'dealValue',
            'dueDate',
            'status',
            'customFields',
            'counterparties',
            'lawyers',
            'defendants'
        ) + Audit.fields()

