from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return self.title
