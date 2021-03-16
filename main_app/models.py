from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    review = models.TextField(max_length=250)
    date = models.DateField("Post Date")
    # adds the many to many association 
    locations = models.ManyToManyField(Location)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

# Create your models here.
class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    # adds the many to many association 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.name}"