from django.db import models

# Create your models here.
class Game(models.Model):

    slug = models.SlugField()
    score = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    # author = models.ForeignKey(User,on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.score
