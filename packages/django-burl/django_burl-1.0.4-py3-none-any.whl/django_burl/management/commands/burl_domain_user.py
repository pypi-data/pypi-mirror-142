from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from django.core.management import BaseCommand
from django.db import IntegrityError

from django_burl.models import BriefURLDomainUser


class Command(BaseCommand):
    help = "manages BriefURLDomainUser objects for burl"

    def add_arguments(self, parser):
        parser.add_argument("action", type=str, help="action to take [ add | ls | rm ]")
        parser.add_argument("--domain", type=str, help="domain name to add user to")
        parser.add_argument(
            "--user", type=str, help="username of user to add/remove to/from domain"
        )
        parser.add_argument(
            "--role",
            type=str,
            help="role for newly added user [ creator | editor | admin ]",
        )

    def handle(self, *args, **options):
        if options["action"] == "add":
            if not options["role"] or not options["user"] or not options["domain"]:
                raise SystemExit(
                    "must specify --role, --user, and --domain with action add"
                )
            try:
                user = get_user_model().objects.get(username=options["user"])
                site = Site.objects.get(domain=options["domain"])
                role = BriefURLDomainUser.Role(options["role"])
            except ObjectDoesNotExist:
                raise SystemExit(f"user or domain does not exist")
            except ValueError:
                raise SystemExit(f"invalid role (must be creator, admin, or editor)")
            try:
                domain_user, created = BriefURLDomainUser.objects.get_or_create(
                    user=user, site=site, role=role
                )
                if created:
                    self.stderr.write(
                        f"added {options['user']} to {options['domain']} as {options['role']}"
                    )
            except IntegrityError:
                raise SystemExit(
                    f"user {options['user']} already exists in site {options['domain']}"
                )

        if options["action"] == "rm":
            if not options["user"] or not options["domain"]:
                raise SystemExit("must specify --user and --domain with action rm")
            try:
                user = get_user_model().objects.get(username=options["user"])
                site = Site.objects.get(domain=options["domain"])
            except ObjectDoesNotExist:
                raise SystemExit(f"user user or domain does not exist")
            try:
                BriefURLDomainUser.objects.get(user=user, site=site).delete()
                self.stderr.write(f"removed {user.username} from {site.domain}")
            except Exception as ex:
                raise SystemExit(
                    f"error deleting user {options['user']} from site {options['site']}: {ex}"
                )

        if options["action"] == "ls":
            for domain_user in BriefURLDomainUser.objects.all():
                self.stdout.write(str(domain_user))
