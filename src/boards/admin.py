from django.contrib import admin
from .models import Board, Topic, Post

admin.site.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name']
    class Meta:
        model = Board

admin.site.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subject']
    class Meta:
        model = Topic

admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'message']
    class Meta:
        model = Post
