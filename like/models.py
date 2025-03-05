from django.db import models
from account.models import User
from blog.models import Blog


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ['user', 'post']

    def __str__(self):
        return f'{self.user} likes {self.post}'