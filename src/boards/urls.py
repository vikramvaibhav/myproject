from django.urls import path
from .views import (
    BoardListView,
    TopicListView,
    PostListView,
    PostUpdateView,
    new_topic,
    reply_topic
    )

app_name = 'boards'

urlpatterns = [
    path('', BoardListView.as_view(), name='home'),
    path('boards/<int:pk>/', TopicListView.as_view(), name='board_topics'),
    path('boards/<int:pk>/new/', new_topic, name='new_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>/', PostListView.as_view(), name='topic_posts'),
    path('boards/<int:pk>/topics/<int:topic_pk>/reply/', reply_topic, name='reply_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/', PostUpdateView.as_view(), name='edit_post'),
]
