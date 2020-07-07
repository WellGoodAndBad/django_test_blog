from django.utils.text import slugify
from time import time


def gen_slug(stg_for_gen: str):
    slug = slugify(stg_for_gen, allow_unicode=True)
    slug += '-' + str(int(time()))

    return slug

