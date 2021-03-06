from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    comments = forms.CharField(
        required=False,
        max_length=150,
        widget=forms.TextInput(attrs={'size':'80'}))
    rating = forms.DecimalField(
        min_value=1,
        max_value=5,
        required=False,
        label="Please Rate between 1 and 5",
        max_digits=2,
        widget=forms.TextInput(attrs={'size': '3'}),
        decimal_places=1)
    nickname = forms.BooleanField(required=False, label='Leave Nickname?')
    anonymous = forms.BooleanField(required=False, label='Stay Anonymous?')

    class Meta:
        model = Comment
        fields = [
            'comments',
            'rating'
        ]

