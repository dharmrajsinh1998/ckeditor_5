from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Article


class ArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # it is required to set it False,
        # otherwise it will throw error in console
        self.fields["text"].required = False

    class Meta:
        model = Article
        fields = '__all__'
        # you can also use CKEditor5Widget in your forms.
        # we don't need it. because we have model form
        # widgets = {
        #     "text": CKEditor5Widget(
        #         attrs={"class": "django_ckeditor_5"}, config_name="extends"
        #     )
        # }
