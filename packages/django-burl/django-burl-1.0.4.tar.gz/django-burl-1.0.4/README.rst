###########
django-burl
###########

``django-burl`` (brief url) is a URL shortening application for inclusion in
django projects. It provides a data model and a simple REST API in addition
to URL redirection capabilities.

If you are looking for a standalone URL shortener that you can quickly run in
a container, *see* `burl <https://github.com/wryfi/burl>`__ for a ready-to-go
reference implementation of ``django-burl``.


Quick Start
===========

1. Install by running ``pip install django-burl`` in your python/django environment

2. Configure django (e.g. in your project's ``settings.py``) as follows: ::

        INSTALLED_APPS = [
            ...,
            "django.contrib.sites",
            "django_filter",
            "rest_framework",
            "django_burl",
        ]

        MIDDLEWARE = [
            ...,
            "django.contrib.sites.middleware.CurrentSiteMiddleware"
        ]

        REST_FRAMEWORK = {
            ...,
            "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
        }


3. Run database migrations, e.g. ``manage.py migrate``.

4. Add the URLs from ``django_burl.api.v2.urls``  or ``django_burl.urls`` to your application's URL structure.

5. Create some Brief URLs in the Django admin (logged in as a superuser).

6. Explore the API. Its URL may vary depending on how you configured your
   project. (HINT: install ``django_extensions`` and then run ``manage.py show_urls``
   to get a full list of your project's URLs if you're not sure.)


Sites & Permissions
===================

``django-burl`` uses the django
`sites framework <https://docs.djangoproject.com/en/4.0/ref/contrib/sites/>`__,
allowing one django instance to host multiple domains. Permissions
to each site are determined by ``BriefURLDomainUser`` objects, which you can create
and manipulate in the Django Admin (as a superuser).

These objects map a user to a site and one of three roles:

* Creator - has the ability to create burls, and to view, modify and delete his/her own burls
* Editor - has creator permissions plus ability to view all burls and modify any burl
* Admin - has editor permissions plus ability to delete a burl

Anonymous requests are denied, and users who are not associated with any
``BriefURLDomainUser`` objects are also denied access.

Requests to the REST API are always scoped by domain based on the request's
``Host`` header. For example, if your django instance has two sites with domains
``abc.test`` and ``xyx.test``, you cannot manipulate the burls for ``abc.test``
by making requests to the API at https://xyz.test; you can only do so through
https://abc.test.

NOTE: Only superusers can modify the owner of a burl, and must take care that the
burl's owner has access to its site via ``BriefURLDomainUser`` objects (neither the
admin interface nor the REST API currently enforces this). Otherwise, the burl
will become manageable only by superusers and will not be accessible to its owner.

Likewise, the burls available to non-superusers in the django admin interface
are also scoped by site: a user working in https://xyz.test/admin will not see
any burls for ``abc.test``, even if both domains are hosted on the same django
instance, and the user has permission to them both. If the user wants to edit
burls in ``abc.test``, it must be done via the https://abc.test/admin interface.

Superusers editing burls in the django admin interface will see all burls from
all domains, where they can change the owner and site/domain for each burl.
Again care must be taken that the burl's owner has access to its site via
``BriefURLDomainUser`` objects (the admin interface does not enforce this).

Django Admin
============

Burls can be managed by non-superusers in the Django admin, by granting the user
*Staff status* and the following *User permissions*:

* ``django_burl | brief url | Can view brief url``

The default redirect for a domain can also be managed (by a site admin) in the
django admin by granting:

* ``django_burl | brief url default redirect | Can view brief url default redirect``

(This is not currently used by ``django-burl`` directly, but may be useful in your
upstream application.)

API Reference
=============

It is assumed that ``django-burl`` will be installed within a larger django project,
and leaves to the project architect the task of integrating it with other API
endpoints and resources.

The API is implemented using
`django rest framework <https://www.django-rest-framework.org/>`__ (DRF). It
follows standard DRF settings and conventions, and should play nice with other
tools in the greater DRF sandbox. You can visit the API root in your browser
for a user-friendly interface.

Brief URLs are represented as JSON objects of the following schema: ::

    {
        "burl": string,
        "url": string,
        "user": int | uuid,
        "description": string,
        "enabled": bool
    }

The following URL endpoints are provided: ::

    /burls (GET, POST, HEAD, OPTIONS)

        GET - list Brief URLs
        POST - create a new Brief URL (JSON body per schema above)

    /burls/<burl> (GET, PUT, PATCH, DELETE, HEAD, OPTIONS)

        GET - return details about the requested Brief URL
        PUT - entirely replace the requested Brief URL (JSON body per schema above)
        PATCH - update the provided fields on the requested Brief URL (JSON body per schema above)
        DELETE - delete the requested Brief URL


Implementation
==============

``django-burl`` implements a URL shortening service by allowing authorized users
to create a brief URL pointing to any other URL.

When creating a brief URL, the user may specify the brief url, which must be
unique within the domain. If the user does not specify a brief URL, one will be
generated by passing a random salt and number into the
`hashids <https://hashids.org/>`__ library until a unique string is found.

The ``HASHID_ALPHABET`` setting determines the characters (as a string) that will
be used to automatically generate burls. The ``BURL_BLACKLIST`` setting is a list
of strings that will not be used when generating burls.

When the brief URL is subsequently requested from ``django-burl``, it returns
a redirect to the original URL.

There are two primary interfaces to burl:

#. the built-in django admin interface (typically at https://abc.test/admin/);
#. a minimal restful API based on
   `django rest framework <https://www.django-rest-framework.org/>`__ (DRF).

New brief URLs can only be created by authenticated users (via session auth
or token auth by default), who must also be granted permission to the relevant
site via ``BriefURLDomainUser`` objects. Permissions and authentication methods
are further extensible via DRF.


Requirements
============

code
----

You will need an existing `Django <https://www.djangoproject.com>`__
project, running at least django 2.2+ and python 3.7+.

In addition, the `sites framework <https://docs.djangoproject.com/en/4.0/ref/contrib/sites>`__
must be installed, and ``CurrentSiteMiddleware`` enabled in your project.

For a standalone url shortener implementing ``django-burl``, see
`burl <https://github.com/wryfi/burl>`__.


database
--------

A PostgreSQL database is recommended for your ``django-burl`` project.
While MySQL variants may also work, ``django-burl`` is tested against and
optimized for postgres.

Note that ``django-burl`` does rely on strong constraints, so sqlite is not
supported.

Follow the standard Django docs for configuring your database engine.


user model
----------

``django-burl`` serializes the user id field in API responses. This imposes
some limitations on the user model that can be used with the package. Namely,
your user model must have an ``id`` field that is either:

- an integer, e.g. ``AutoField`` (as found on the default django user model),
  ``BigAutoField``, or ``IntegerField``
- or a UUID, e.g. ``UUIDField``

User models that do not conform to the above specification are not supported.


Installation
============

``django-burl`` is made to be installed via the standard python installation methods.
You can install it as simply as running::

    pip install django-burl

It is recommended, of course, that you use ``django-burl`` in a virtualenv or
Docker container.

Then, configure your ``settings.py`` as follows: ::

    INSTALLED_APPS = [
        ...,
        "django.contrib.sites",
        "django_filter",
        "rest_framework",
        "django_burl",
    ]

    MIDDLEWARE = [
        ...,
        "django.contrib.sites.middleware.CurrentSiteMiddleware"
    ]

    REST_FRAMEWORK = {
        ...,
        "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend", ... ],
    }

Next, run the database migrations to create the necessary tables, using your
project's management script::

    manage.py migrate

You should now see the database tables in the django admin after restarting
your application.

Finally, configure API routes by including ``django_burl.urls`` in your application's
URL configuration.

Configuration
=============

``django-burl`` reads its configuration from the standard django settings module,
which is typically extended in a ``settings.py`` file (or whatever module is
specified in the ``$DJANGO_SETTINGS_MODULE`` environment variable). More relevant
settings include: ::

    # list of strings that cannot be used as brief URLs;
    # subtracting from the below defaults is inadvisable, but extend at will!
    BURL_BLACKLIST = ["admin", "api", "static", "media"]

    # the characters available for generating BURLs
    HASHID_ALPHABET = "abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ0123456789"

    # when there are more than this number of burls, the django admin gets its count of
    # objects using a less accurate estimate from postgres, rather than count(*);
    # if another db is used, this setting is ignored.
    ROUGH_COUNT_MIN = 1000

    # the configured user model (must have an id that is an int or a uuid)
    AUTH_USER_MODEL = "myapp.models.user"

    # you can extend DRF settings to your liking ...
    REST_FRAMEWORK = {
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework.authentication.SessionAuthentication",
            "rest_framework.authentication.TokenAuthentication",
        ),
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
        "PAGE_SIZE": 20,
        "DEFAULT_PARSER_CLASSES": [
            "rest_framework.parsers.JSONParser",
        ],
        "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    }

``django_burl.conf.settings`` extends ``django.conf.settings``, supplying default
values for ``BURL_BLACKLIST``, ``HASHID_ALPHABET`` and ``ROUGH_COUNT_MIN`` if
they are not already provided. Modules throughout this library therefore import
from ``django_burl.conf.settings`` instead of ``django.conf.settings``.
