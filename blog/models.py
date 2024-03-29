from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Exponant(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.TextField()
    img = models.ImageField(upload_to='exponant/')

    def __str__(self):
        return self.title
class ExponantComment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User,
                               on_delete=models.SET_NULL, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    exponant = models.ForeignKey(Exponant, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.exponant)