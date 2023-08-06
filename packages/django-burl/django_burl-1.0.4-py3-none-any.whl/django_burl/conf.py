from django.conf import settings

if not hasattr(settings, "BURL_BLACKLIST"):
    settings.BURL_BLACKLIST = ["admin", "api", "static", "media"]

if not hasattr(settings, "ROUGH_COUNT_MIN"):
    settings.ROUGH_COUNT_MIN = 1000

if not hasattr(settings, "HASHID_ALPHABET"):
    settings.HASHID_ALPHABET = (
        "abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ0123456789"
    )
