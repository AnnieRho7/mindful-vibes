from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = (
    (0, "Draft"),
    (1, "Published"),
    (2, "Pending Approval"),
)

class Post(models.Model):
    """
    Model representing a blog post.

    Attributes:
        title (str): The title of the post, must be unique.
        slug (str): A URL-friendly version of the title, must be unique.
        author (User): The author of the post, linked to the User model.
        featured_image (CloudinaryField): The featured image for the post.
        content (str): The main content of the post.
        created_on (datetime): The date and time the post was created.
        status (int): The status of the post, defined by STATUS choices.
        approved (bool): A flag indicating whether the post is approved.
        excerpt (str): A short summary of the post, can be blank.
        updated_on (datetime): The date and time the post was last updated.
        featured (bool): A flag indicating whether the post is featured.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    @classmethod
    def get_featured_posts(cls):
        """Class method to get featured posts."""
        return cls.objects.filter(status=1, featured=True).order_by('-created_on')[:3]
    
class Comment(models.Model):
    """
    Model representing a comment on a blog post.

    Attributes:
        post (Post): The post that this comment belongs to.
        author (User): The author of the comment, linked to the User model.
        body (str): The content of the comment.
        approved (bool): A flag indicating whether the comment is approved.
        created_on (datetime): The date and time the comment was created.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class Subscriber(models.Model):
    """
    Model representing a subscriber's email for newsletters or updates.

    Attributes:
        email (str): The email address of the subscriber, must be unique.
    """
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
