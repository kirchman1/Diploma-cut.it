from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView
from main.models import Link


class LinkAdd(CreateView):
    model = Link
    template_name = 'main/links.html'

    fields = ['link', 'slug']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(LinkAdd, self).get_context_data(**kwards)

        ctx['title'] = 'Your Links'
        ctx['links'] = Link.objects.all()
        return ctx


def about(request):
    return render(request, 'main/about.html', {'title': 'About us'})


def home(request):
    return render(request, 'main/home.html', {'title': 'Main page'})
