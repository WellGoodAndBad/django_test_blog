from django.contrib import admin

from .models import PostBlog, Comment


admin.site.register(PostBlog)

admin.site.register(Comment)
