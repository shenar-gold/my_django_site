from django import forms
from .models import Post, Comment
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, failield
# from crispy_forms.bootstrap import (PrependedText, PrependedAppendedText, FormActions)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post;
        fields = ('author','title', 'text');


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment;
        fields = ('text',);
