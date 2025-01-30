from django import forms
from .models import Comment, Post
from django.core.exceptions import ValidationError

class CommentForm(forms.ModelForm):
    """
    Form for users to submit comments.
    Field: body.
    """
    class Meta:
        model = Comment
        fields = ('body',)
        error_messages = {
            'body': {
                'required': "Comment cannot be empty."
            }
        }

    def clean_body(self):
        """Validate comment body length"""
        body = self.cleaned_data.get('body')
        if len(body) < 2:
            raise ValidationError("Comment must be at least 2 characters long.")
        if len(body) > 1000:
            raise ValidationError("Comment cannot be longer than 1000 characters.")
        return body


class PostForm(forms.ModelForm):
    """
    Form for users to create or edit a blog post.
    Fields: title, slug, featured_image, content, excerpt.
    """
    # Add help text for slug field
    slug = forms.SlugField(
        help_text="URL-friendly name using only letters, numbers, underscores or hyphens.",
        error_messages={
            'invalid': "Please use only letters, numbers, underscores or hyphens."
        }
    )

    class Meta:
        model = Post
        fields = ['title', 'slug', 'featured_image', 'content', 'excerpt']
        error_messages = {
            'title': {
                'required': "Title is required.",
                'unique': "A post with this title already exists.",
                'max_length': "Title must be less than 200 characters."
            },
            'content': {
                'required': "Content is required."
            }
        }

    def clean_title(self):
        """Validate title length"""
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise ValidationError("Title must be at least 3 characters long.")
        return title

    def clean_content(self):
        """Validate content length"""
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise ValidationError("Content must be at least 10 characters long.")
        return content

    def clean_excerpt(self):
        """Validate excerpt length"""
        excerpt = self.cleaned_data.get('excerpt')
        if excerpt and len(excerpt) > 200:
            raise ValidationError("Excerpt must be less than 200 characters.")
        return excerpt