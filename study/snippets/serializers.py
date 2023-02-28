from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    snippets = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name='snippet-detail',
                                                   read_only=True)

    """
        owner = models.ForeignKey('auth.User', 
        related_name='snippets',  --->
        on_delete=models.CASCADE)

    """

    class Meta:
        model = User
        # fields = ['id', 'username', 'snippets']
        fields = ['url', 'id', 'username', 'snippets']


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight',
                                                     format='html')

    class Meta:
        model = Snippet
        # fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']
