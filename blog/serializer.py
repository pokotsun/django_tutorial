# coding: utf-8


from rest_framework import serializers

from .models import User, Entry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # APIとして出力したいfieldのタプル
        fields = ('id', 'name', 'mail',)

class CustomUserSerializer(UserSerializer):
    # ここでこのように宣言することでモデル外の変数をcolumnの一部のように扱える
    value = serializers.SerializerMethodField()
     
    class Meta:
        model = User
        # APIとして出力したいfieldのタプル
        fields = ('id', 'name', 'mail', 'value')

    # このget_methodで取得が可能となる
    def get_value(self, obj):
        #return obj 
        return {"id": "あいうえお", "gorira": "かきくけこ"}
        #return obj.name
    

class EntrySerializer(serializers.ModelSerializer):
    # authorのserializerを上書きすることっで、入れ子にできる
    author = UserSerializer()

    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author')
