from django.contrib.auth.models import User

from rest_framework import serializers

from webtweets.models import Tweet


class TweetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tweet
        fields = ('text', 'user', 'timestamp')

    def validate_text(self, attrs, source):
        value = attrs[source]
        if len(value) < 5:
            raise serializers.ValidationError(
                "Text is too short!")
        return attrs


class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'last_login')