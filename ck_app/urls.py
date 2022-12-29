from django.urls import path
from .views import AddArticle, ArticleDetail

urlpatterns = [
    path('', AddArticle.as_view(), name="add_article"),
    path('article/<int:pk>/', ArticleDetail.as_view(), name="article_detail")
]
