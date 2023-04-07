from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class NewsSendForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    title = forms.CharField(required=False, widget=forms.Textarea)
    link = forms.CharField(required=False, widget=forms.Textarea)
    # comments = forms.CharField(required=False,widget=forms.Textarea)


class SearchForm(forms.Form):
    query = forms.CharField(label=False)
    query.widget.attrs['placeholder'] = "Type & Hit Enter..."
