import string
import random
from django.utils.text import slugify


def random_string_generator(size=4, chars=string.ascii_lowercase + string.digits):
    '''
    Generate random string for making unique slugs.
    It generates 4 random chars by default.
    accepts 2 optional parameters
    @param size
    @param chars
    '''
    string_list = [random.choice(chars) for _ in range(size)]
    return ''.join(string_list) 


def unique_slug_generator(instance):
    '''
    It acceps 1 positional argument (instance).
    It assumes your model has a slug and name fields
    '''
    model = instance.__class__ # model of the instance
    slug = slugify(instance.name)
    if model.objects.filter(slug=slug).exists():
        new_slug = f'{instance.slug}-{random_string_generator()}'
        return new_slug
    return slug
