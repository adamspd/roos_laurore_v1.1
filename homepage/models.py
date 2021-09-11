from django.db import models
from django.utils.timezone import now

# Create your models here.


class Album(models.Model):
    album_title = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.album_title


def get_path(instance, filename):
    return '{0}/{1}'.format(instance.file.album_title, filename)


class Photo(models.Model):
    CATEGORY =(
        ('raw', 'raw'),
        ('jpg', 'jpg'),
        ('psd', 'psd')
    )

    name = models.CharField(null=True, max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='Homepage', null=True, blank=True)
    file_type = models.CharField(max_length=200, null=True, choices=CATEGORY)
    is_favorite = models.BooleanField(default=False)
    date_uploaded = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.album) + "ID.{:0>3}".format(self.id)

    def album_name(self):
        return str(self.album.album_title)




