from random import choices

from django import forms

from form.models import Tag, Category, Portfolio, Post


class CreateTagForm(forms.Form):
    title = forms.CharField(label='Your name', max_length=255)

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category

class CreatePortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
class CreatePostForm(forms.ModelForm):
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


class SimpleForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["title"]


# class CommentForm(forms.Form):
#     name = forms.CharField(initial='class')
#     url = forms.URLField()
#     comment = forms.CharField()




