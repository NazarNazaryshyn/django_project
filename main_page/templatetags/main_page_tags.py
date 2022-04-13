from django import template
from main_page.models import *

register = template.Library()


@register.simple_tag()
def get_customer():
    return Customer.objects.all()

