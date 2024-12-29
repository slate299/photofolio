from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the message is created

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Photo(models.Model):
    CATEGORY_CHOICES = [
        ('birds', 'Birds'),
        ('wildlife', 'Wildlife'),
        ('nature', 'Nature'),
        ('events', 'Events'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title