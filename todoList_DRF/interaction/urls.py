from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .api_views import LikeViewSet, BookmarkViewSet, CommentViewSet, CommentLikeViewSet
from .views import todo_detail_with_interaction

router = DefaultRouter()
router.register(r"likes", LikeViewSet, basename="likes")
router.register(r"bookmarks", BookmarkViewSet, basename="bookmarks")
router.register(r"comments", CommentViewSet, basename="comments")
router.register(r"commentlikes", CommentLikeViewSet, basename="commentlikes")


app_name = "interaction"


urlpatterns =[
    path('', include(router.urls)),
    path('todo/detail/<int:pk>/', todo_detail_with_interaction, name='todo_detail'),
]