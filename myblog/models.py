from django.db import models
from django.utils import timezone

class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Technology'),
        ('health', 'Health'),
        ('sports', 'Sports'),
        ('education', 'Education'),
        ('business', 'Business'),
    ]
    
    image = models.ImageField(upload_to='blog_images/')
    text = models.CharField(max_length=500)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='tech')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text  # Returns the first 50 characters of the blog text
