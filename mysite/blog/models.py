from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    picture = models.ImageField(blank=True, null=True)
    blogger = models.CharField(max_length = 120)
    datetime = models.DateTimeField(default = timezone.now, blank=True )

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("Blog:blogDetails", kwargs={"my_id": self.id})

    # def save(self,**kwargs):
    #   if kwargs.has_key('request') and self.blogger is None:
    #         request = kwargs.pop('request')
    #         self.blogger= request.user
    #   super(Blog, self).save(**kwargs)
