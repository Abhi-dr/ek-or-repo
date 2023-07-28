from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField()
    
    choices = (
        ("Maths", "Maths"),
        ("English", "English"),
    )
    
    subject = models.CharField(max_length=30, choices=choices)
    
    def __str__(self):
        return self.title
    

