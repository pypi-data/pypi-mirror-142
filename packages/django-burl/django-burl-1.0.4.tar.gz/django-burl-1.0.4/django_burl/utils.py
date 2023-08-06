import secrets

from hashids import Hashids

from django_burl.conf import settings


def make_burl(ceiling=1000):
    """
    Generates a non-unique burl short url

    :param ceiling: maximum integer for generating random number
    :return: burl short url
    :rtype: str
    """
    salt = secrets.token_hex(4)
    hasher = Hashids(salt=salt, alphabet=settings.HASHID_ALPHABET)
    random = secrets.randbelow(abs(ceiling) + 1000)
    return hasher.encode(random)
