from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# create class to create serialized models
class SnippetSerializer(serializers.Serializer):
    # initialize the fields
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'linenos', 'language', 'style')