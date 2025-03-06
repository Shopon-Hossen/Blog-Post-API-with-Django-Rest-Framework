from django.db import models
from account.models import User
from tag.models import Tag


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blogs'
    )
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # Custom method to get similar objects
    def get_similar_blogs(self):
        return Blog.objects.filter(tags__in=self.tags.all()).exclude(id=self.id).distinct()[:5] # First 5 objects