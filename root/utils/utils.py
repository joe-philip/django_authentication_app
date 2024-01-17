from datetime import datetime

from django.utils.text import slugify
from pytz import timezone


def slug_generate(key: str = 'slug') -> str:
    return slugify(f'{key}-{datetime.now(tz=timezone("Asia/Calcutta"))}')
