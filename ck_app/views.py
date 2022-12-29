from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import ArticleForm
from .models import Article


class AddArticle(SuccessMessageMixin, CreateView):
    form_class = ArticleForm
    model = Article
    template_name = "add_article.html"
    success_message = "Added Succesfully"

    def get_success_url(self):
        return reverse('add_article')


class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = "article_detail.html"
