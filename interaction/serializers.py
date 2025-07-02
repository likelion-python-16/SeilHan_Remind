from .models import Like, Bookmark, Comment, CommentLike
from rest_framework import serializers


class LikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    todo_name = serializers.CharField(source="todo.name", read_only=True)

    class Meta:
        model = Like
        fields = ["id", "todo", "todo_name", "user", "username", "is_like"]
        read_only_fields = ["user"]


class BookmarkSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    todo_name = serializers.CharField(source="todo.name", read_only=True)

    class Meta:
        model = Bookmark
        fields = ["id", "todo", "todo_name", "user", "username", "is_marked"]
        read_only_fields = ["user"]


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    todo_name = serializers.CharField(source="todo.name", read_only=True)

    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "todo", "todo_name", "user", "username", "content", "created_at", "like_count"]
        read_only_fields = ["todo", "user", "created_at"]

    def get_like_count(self, obj):
        return obj.likes.count()
    
    def get_is_liked(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False
    

class CommentLikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    comment_content = serializers.CharField(source="comment.content", read_only=True)

    class Meta:
        model = CommentLike
        fields = ["id", "user", "username", "comment", "comment_content", "is_like"]
        read_only_fields = ["user"]