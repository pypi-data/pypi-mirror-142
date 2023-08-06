from rest_framework import serializers

from django_burl.conf import settings
from django_burl.models import BriefURL


class BurlSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = BriefURL
        fields = ("burl", "url", "user", "description", "enabled", "created", "updated")

    def validate_burl(self, value):
        if value in settings.BURL_BLACKLIST:
            raise serializers.ValidationError(
                f'burl "{value}" is blacklisted by BURL_BLACKLIST setting'
            )
        return value


class BurlSerializer(BurlSerializerBase):
    user = serializers.IntegerField(required=False, source="user.id")


class BurlUserUUIDSerializer(BurlSerializerBase):
    user = serializers.UUIDField(required=False, source="user.id")
