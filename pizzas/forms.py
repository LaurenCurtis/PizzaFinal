from django import forms
from .models import Comment,Pizza

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']
        label = {"Comment:":""}