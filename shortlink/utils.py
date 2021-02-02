from random import choices
import string
from .models import Url


def get_short_url():
    char = string.digits + string.ascii_letters
    short_url = ''.join(choices(char, k=6))

    url = Url.objects.filter(short_url=short_url)

    if url:
        short_url = get_short_url()

    return short_url
