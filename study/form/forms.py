from random import choices

from django import forms

from form.models import Tag, Category, Portfolio, Post


class CreateTagForm(forms.Form):
    title = forms.CharField(label='Your name', max_length=255)


# class CreatePostForm(forms.Form):
#     # categories = Category.objects.all()
#     # def get_context(self):
#     def __init__(self, user, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.user = user.id
#
#     title = forms.CharField(label='title', max_length=255)
#     text = forms.CharField(label='text', widget=forms.Textarea)
#     author = forms.ModelChoiceField(label='author', queryset=Portfolio.objects.filter(author__id=user))
#     category = forms.ModelChoiceField(label='category', queryset=Category.objects.all())
#     tags = forms.ModelMultipleChoiceField(label='tags', queryset=Tag.objects.all())

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
