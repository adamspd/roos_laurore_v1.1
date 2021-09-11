from django.db import models
from django.conf import settings


# Create your models here.


class Photo(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)
    file = models.ImageField(upload_to='Client', null=True, blank=True)

    def __str__(self):
        return 'userID' + str(self.owner_id) + '-' + self.name
