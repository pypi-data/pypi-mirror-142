from contextlib import contextmanager

import psycopg2
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist

from django.core.management import BaseCommand
from django.conf import settings

from django_burl.models import BriefURL


class Command(BaseCommand):
    help = "migrates redirects from old model to new - postgres only"

    def add_arguments(self, parser):
        parser.add_argument(
            "domain", type=str, help="domain name to add imported burls to"
        )

    def handle(self, *args, **options):
        if (
            settings.DATABASES["default"]["ENGINE"]
            != "django.db.backends.postgresql_psycopg2"
        ):
            raise SystemExit("this tool only works for postgresql_psycopg2 databases")
        try:
            site = Site.objects.get(domain=options["domain"])
        except ObjectDoesNotExist:
            raise SystemExit(f"site matching domain {options['domain']} not found")
        with psyco_connect(
            settings.DATABASES["default"]["NAME"],
            settings.DATABASES["default"]["USER"],
            settings.DATABASES["default"]["PASSWORD"],
            settings.DATABASES["default"]["HOST"],
            settings.DATABASES["default"]["PORT"],
        ) as cxn:
            cursor = cxn.cursor()
            cursor.execute(
                "SELECT id, url, burl, description, user_id, created, updated, enabled FROM redirects_redirect"
            )
            for row in cursor.fetchall():
                try:
                    burl, created = BriefURL.objects.get_or_create(
                        id=row[0],
                        url=row[1],
                        burl=row[2],
                        description=row[3],
                        user=get_user_model().objects.get(id=row[4]),
                        created=row[5],
                        updated=row[6],
                        enabled=row[7],
                        site=site,
                    )
                    if created:
                        self.stderr.write(
                            f"migrated burl /{burl.burl} to {site.domain}/{burl.burl}"
                        )
                except ObjectDoesNotExist:
                    raise SystemExit(f"could not find user matching {row[3]}")


@contextmanager
def psyco_connect(name, user, password, host, port):
    cxn = psycopg2.connect(
        database=name, user=user, password=password, host=host, port=port
    )
    try:
        yield cxn
    finally:
        cxn.close()
