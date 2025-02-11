from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(max_length=500)
    website = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name

class WatchList(models.Model):
    title= models.CharField(max_length=50)
    storyline = models.TextField(max_length= 500)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField(max_length=500, null=True)
    active = models.BooleanField(default=True) #valid or invalid review
    watch = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating) + " | " + self.watch.title