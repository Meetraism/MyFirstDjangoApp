from django.contrib import admin
from MyFirstDjangoApp.models import Post, Comment


# Registering the Post model
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'content', 'image') # Columns to display in the list view
    search_fields = ('title', 'content')

# Registering the Comment model
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'post', 'reply_to')
    search_fields = ('content',)

# Register the models with the admin site
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)