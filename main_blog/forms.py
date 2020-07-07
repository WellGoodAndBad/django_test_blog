from django import forms
from .models import PostBlog, Comment


class PostBlogModelForm(forms.ModelForm):
    class Meta:
        model = PostBlog
        fields = ['title', 'text_post', 'tags']
        labels = {'title': 'Имя поста', 'text_post': 'Текст поста', 'tags': 'Тэги поста'}
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'text_post': forms.Textarea(attrs={'class': "form-control"}),
            'tags': forms.TextInput(attrs={'class': "form-control"}),
                   }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

