from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title' , 'text','created_date' ,'author')
        #image = forms.FileField()


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )
