from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Pygment module is only needed for style and code highlighting
# Crearte a list of lexers
LEXERS = [item for item in get_all_lexers() if item[1]]
# Created a list of all languages from lexers
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# get the style for languages
STYLE_CHOICES = sorted((item,item) for item in get_all_styles())


# Create a class snippets

class Snippet(models.Model):
    '''
    This are the members forr the class the class is for creating styles for the languages
    '''

    created = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default="frindly", max_length=100)

    class Meta:
        ordering = ("created",)
