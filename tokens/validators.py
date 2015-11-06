from re import match
from django.core.exceptions import ValidationError


def validate_token_key(value):
    result = match('^[a-zA-Z][a-zA-Z0-9-_]*$', value)

    if not result:
        raise ValidationError('%s not a valid token.' % value)
