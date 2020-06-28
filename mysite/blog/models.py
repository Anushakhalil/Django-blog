from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    picture = models.ImageField(blank=True, null=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("Article:article-detail", kwargs={"id": self.id})
