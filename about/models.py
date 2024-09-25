from django.db import models

# Create your models here.


class About(models.Model):
    """
    Model representing information about the application.

    Attributes:
        title (str): The title of the about section.
        updated_on (datetime): The date and time the content was last updated.
        content (str): The detailed content of the about section.
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class CollaborateRequest(models.Model):
    """
    Model representing a request to collaborate.

    Attributes:
        name (str): The name of the person requesting collaboration.
        email (str): The email address of the requester.
        message (str): The message or proposal from the requester.
        read (bool): A flag indicating whether the request has been read.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"