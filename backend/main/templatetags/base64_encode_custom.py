from django import template
import base64

register = template.Library()

@register.filter
def base64_encode_custom(data):
    return base64.b64encode(data).decode('utf-8')