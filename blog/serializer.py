# coding: utf-8


from rest_framework import serializers

from .models import User, Entry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'mail')


class EntrySerializer(serializers.ModelSerializer):
    # authorのserializerを上書きすることっで、入れ子にできる
    author = UserSerializer()

    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author')
