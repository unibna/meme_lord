from django import forms
from .models import Comment

# class PostCreateForm(forms.ModelForm):

#     class Meta(forms.ModelForm.Meta):

#         model = Post
#         fields = '__all__'

class CommentCreateForm(forms.ModelForm):


    class Meta:

        model = Comment
        fields = ['content']
