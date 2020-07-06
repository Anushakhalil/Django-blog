from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Blog(models.Model):
    categories=(
        ("Category1", "Category1"),
        ("Category2", "Category2")
    )
    title = models.CharField(max_length=120)
    content = models.TextField()
    picture = models.ImageField(blank=True, null=True)
    blogger = models.CharField(max_length = 120, default= "---")
    datetime = models.DateTimeField(default = timezone.now, blank=True )
    cat = models.CharField(max_length=120, choices=categories, default="--")

    def get_absolute_url(self):
        
        return reverse("Blog:blogDetails", kwargs={"my_id": self.id})

    def catKaURL(self):

        # return self.cat

        return reverse("Blog:catDetails", kwargs={"catName":self.cat})


    # def save(self,**kwargs):
    #   if kwargs.has_key('request') and self.blogger is None:
    #         request = kwargs.pop('request')
    #         self.blogger= request.user
    #   super(Blog, self).save(**kwargs)
