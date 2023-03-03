from random import choices

import captcha as captcha
from captcha.fields import CaptchaField
from django import forms
from django.forms import formset_factory

from form.models import Tag, Category, Portfolio, Post


class CreateTagForm(forms.Form):
    title = forms.CharField(label='Tag_name', max_length=255)


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CreatePortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['nickname']


class CreatePostForm(forms.ModelForm):
    title = forms.CharField(label='Post title', max_length=255, help_text='Post title')
    author = forms.ModelChoiceField(
        queryset=None,
        empty_label=None,
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Portfolio.objects.filter(author=user)

    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'category', 'tags']


class CommentForm(forms.Form):
    name = forms.CharField(initial='class')
    url = forms.URLField()
    comment = forms.CharField()


CreateCategoryFormFactory = forms.modelform_factory(Category,
                                                    fields=('title',),
                                                    labels={'title': 'Category_name'},
                                                    help_texts={"title": "name of category"},
                                                    )


# CategoryFormSet = forms.modelformset_factory(Category, CreateCategoryForm, extra=3)

class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=20, label='Keyword')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Post')

    captcha = CaptchaField(error_messages={'invalid': 'Wrong captcha'},
                           # generator='captcha.helpers.math_challenge'
                           )
