from django.db import models

# Create your models here.
from django.db import models


PICKER_CHOICES = (
    ('comments','Comments'),
    ('likes', 'Likes'),
    ('mentions','Mentions'),    
)


class insta_model(models.Model):
    insta_url = models.CharField(max_length=500)
    picker_kind = models.CharField(max_length=8, choices=PICKER_CHOICES, default='comments')
    number_of_winers = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
        return self.insta_url


