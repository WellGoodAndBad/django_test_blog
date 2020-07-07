from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from .utils import gen_slug


class PostBlog(models.Model):
    title = models.CharField("Заголовок", max_length=250)
    text_post = models.TextField("Содержание", max_length=10000, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main_blog:post_page', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = gen_slug(self.title)

        super().save(*args, **kwargs)

    def get_comments(self):
        return self.comment_set.all()


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=1000, blank=False)
    post = models.ForeignKey(PostBlog, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
