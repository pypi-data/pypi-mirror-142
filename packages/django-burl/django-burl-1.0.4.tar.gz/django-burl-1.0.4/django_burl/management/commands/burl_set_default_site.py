from django.contrib.sites.models import Site
from django.core.management import BaseCommand

from django_burl.conf import settings


class Command(BaseCommand):
    help = "Set parameters of the default django.contrib.sites Site"

    def add_arguments(self, parser):
        parser.add_argument("domain", type=str, help="domain name of the site")
        parser.add_argument(
            "--name", type=str, help="friendly name of the site instance"
        )

    def handle(self, *args, **options):
        site_id = settings.SITE_ID if hasattr(settings, "SITE_ID") else None
        try:
            if site_id:
                site = Site.objects.get(id=site_id)
            else:
                site = Site.objects.get(id=1)
        except Site.DoesNotExist:
            site = Site.objects.first()
        if not site:
            if site_id:
                site, _ = Site.objects.get_or_create(id=site_id)
            else:
                site, _ = Site.objects.get_or_create(domain=options["domain"])
        site.name = options["name"] if options["name"] else site.name
        site.domain = options["domain"] if options["domain"] else site.domain
        site.save()
