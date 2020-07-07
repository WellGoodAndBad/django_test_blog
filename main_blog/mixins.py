from django.http import Http404


class EditDeletMixin:
    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        return qs.filter(slug__iexact=self.kwargs['slug'])

    def get(self, request, *args, **kwargs):
        if self.model.objects.get(slug=self.kwargs['slug']).owner != self.request.user:
            raise Http404
        else:
            return super().get(request, *args, **kwargs)