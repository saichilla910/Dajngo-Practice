from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,null=True,blank=True)

    AboutUs = models.CharField(max_length=1000, blank=True)

    Description = models.TextField(blank=True)

    date_on_posted = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(
        upload_to='profiles',
        default='default/defaultProfile.png',)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image and hasattr(self.image, 'path'):
            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)