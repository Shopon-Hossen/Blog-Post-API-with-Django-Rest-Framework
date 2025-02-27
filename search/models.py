from django.db import models
from account.models import User


class Search(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='search'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
