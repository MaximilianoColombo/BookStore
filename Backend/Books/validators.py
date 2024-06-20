from django.core.exceptions import ValidationError
from django.utils import timezone

#Validators
def validateYearNotInFuture(value):
    currentYear = timezone.now().year
    if value > currentYear:
        raise ValidationError(
            'El año no puede ser superior al año actual.'
        )

