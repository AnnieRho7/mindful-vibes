from django import forms
from .models import Comment
from .models import Post


class CommentForm(forms.ModelForm):
    """
    Form for users to submit comments.
    Field: body.
    """
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """
    Form for users to create or edit a blog post.
    Fields: title, slug, featured_image, content, excerpt.
    """
    class Meta:
        model = Post
        fields = ['title', 'slug', 'featured_image', 'content', 'excerpt']
