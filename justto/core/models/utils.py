from django.core.validators import MinValueValidator
from django.db import models


class MoneyField(models.DecimalField):
	def __init__(self, *args, **kwargs):
		kwargs['validators'] = [MinValueValidator(0)]
		kwargs['decimal_places'] = 5
		kwargs['max_digits'] = 25
		kwargs['default'] = 0
		super(MoneyField, self).__init__(*args, **kwargs)