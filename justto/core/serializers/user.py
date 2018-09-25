from rest_framework import serializers

from ..models.user import *
from ..models.audit import *


class UserSerializer(serializers.ModelSerializer):
    customFields = serializers.HStoreField()

    class Meta:
        model = User
        fields = (
            'id',
            'person',
            'name',
            'legalId',
            'username',
            'customFields'
        ) + Audit.fields()

