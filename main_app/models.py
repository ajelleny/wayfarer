from django.db import models
from django.contrib.auth.models import User

# LOCATION = (
#     ('N', 'New York'),
#     ('L', 'London'),
#     ('S', 'San Francisco')
# )

# Create your models here.
class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    # adds the many to many association 
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, null=False, through="Post")
    
    def __str__(self):
        return f"{self.city}, {self.country}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    review = models.TextField(max_length=250)
    date = models.DateField("Post Date")
    # adds the many to many association 
    # locations = models.ManyToManyField(Location)
    location = models.ForeignKey(Location, default=1, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"





# Create your models here.


