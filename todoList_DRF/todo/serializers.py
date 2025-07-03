from rest_framework.serializers import ModelSerializer
from .models import Todo
from rest_framework import serializers


class TodoSerializer(ModelSerializer):
    is_liked = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    is_bookmarked = serializers.SerializerMethodField()
    bookmark_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = "__all__"
    

    # 직접추가
    def get_is_liked(self, obj):
        user = self.context['request'].user
        return obj.like_set.filter(user=user, is_like=True).exists()

    def get_like_count(self, obj):
        return obj.like_set.filter(is_like=True).count()
        # fields = ["name", "description", "complete", "exp", "completed_at", "created_at", "updated_at"]
        # exclude = ["completed_at", "exp",]

    def get_is_bookmarked(self, obj):
        user = self.context['request'].user
        return obj.bookmark_set.filter(user=user, is_marked=True).exists()
    
    def get_bookmark_count(self, obj):
        return obj.bookmark_set.filter(is_marked=True).count()
    
    def get_comment_count(self, obj):
        return obj.comment_set.count()