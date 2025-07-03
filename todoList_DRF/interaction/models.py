from django.db import models
from todo.models import Todo
from django.contrib.auth.models import User

# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)

    class Meta:
        unique_together = ("user", "todo")
        # todo, user 속성은 중복 데이터를 아예 저장하지 못하게 막아주는 제약조건

    def __str__(self):
        return f"{self.user.username} ❤️ {self.todo.name}"


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    is_marked = models.BooleanField(default=True)

    class Meta:
        unique_together = ("user", "todo")
        # todo, user 속성은 중복 데이터를 아예 저장하지 못하게 막아주는 제약조건

    def __str__(self):
        return f"{self.user.username} ❤️ {self.todo.name}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, through="CommentLike", related_name="liked_comments", blank=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"
    

class CommentLike(models.Model):
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
    is_like = models.BooleanField(default=True)

    class Meta:
        unique_together = ("user", "comment")

    def __str__(self):
        return f"{self.user.username} ❤️ {self.comment.id}"