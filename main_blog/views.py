from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView
from taggit.models import Tag
from django.views.generic import DeleteView
from .models import PostBlog
from .forms import PostBlogModelForm, CommentForm
from .mixins import EditDeletMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(ListView):
    model = PostBlog
    template_name = "main_blog/home.html"
    context_object_name = "posts"
    paginate_by = 10
    ordering = ['-date_create']

    def get_queryset(self, **kwargs):
        obj_list = super().get_queryset()
        search_query = self.request.GET.get('searching_post', '')
        if search_query:
            obj_list = obj_list.filter(Q(title__icontains=search_query) | Q(text_post__icontains=search_query))
        else:
            slug = self.kwargs.get('slug')
            if slug:
                tag = get_object_or_404(Tag, slug=slug)
                obj_list = obj_list.filter(tags__in=[tag])
        return obj_list


class PostView(DetailView):
    model = PostBlog
    template_name = 'main_blog/post_page.html'
    context_object_name = 'post'

    def get_queryset(self):
        return self.model.objects.filter(slug=self.kwargs['slug'])


class NewPost(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('main_blog:home_page')
    form_class = PostBlogModelForm
    template_name = 'main_blog/add_post.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class EditPost(EditDeletMixin, UpdateView):
    model = PostBlog
    fields = ['title', 'text_post', 'tags']
    template_name = 'main_blog/edit_page.html'
    context_object_name = 'post'


class DeletePost(LoginRequiredMixin, EditDeletMixin, DeleteView):
    model = PostBlog
    template_name = 'main_blog/post_delete.html'
    success_url = reverse_lazy('main_blog:home_page')
    context_object_name = 'post'


class AddComment(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    model = PostBlog

    def get_success_url(self):
        post = self.model.objects.get(id=self.kwargs['pk'])
        return post.get_absolute_url()

    def form_valid(self, form):
        post = self.model.objects.get(id=self.kwargs['pk'])
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.post = post
        self.object.save()

        return super(AddComment, self).form_valid(form)
