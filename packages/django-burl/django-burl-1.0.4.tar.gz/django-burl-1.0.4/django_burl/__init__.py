default_app_config = "django_burl.apps.DjangoBurlConfig"

try:
    from django.conf import settings
    from django.core.exceptions import ImproperlyConfigured

    for appname in [
        "django.contrib.sites",
        "django_filters",
        "django_burl",
        "rest_framework",
    ]:
        if appname not in settings.INSTALLED_APPS:
            raise ImproperlyConfigured(
                f"{appname} must be present in the INSTALLED_APPS setting"
            )

    for ware in ["django.contrib.sites.middleware.CurrentSiteMiddleware"]:
        if ware not in settings.MIDDLEWARE:
            raise ImproperlyConfigured(
                f"{ware} must be present in the MIDDLEWARE setting"
            )

except AttributeError as ex:
    raise ImproperlyConfigured(f"{ex} - is django configured properly?")

except ImportError:
    import logging

    logger = logging.getLogger(__name__)
    logger.warning("django does not appear to be installed")
