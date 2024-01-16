from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PostModel(models.Model):
    user = models.ForeignKey(User, related_name='post',on_delete=models.CASCADE)
    caption = models.CharField(max_length=3000)
    created_on = models.DateTimeField(auto_now_add=True)
    # like_dislike = models.OneToOneField(LikeDislikeModel,on_delete = models.CASCADE,null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    post_image = models.ImageField(upload_to='post/media/images/',null=True,blank=True)
    post_like = models.IntegerField(default=0,null=True,blank=True)
    post_dislike = models.IntegerField(default=0,null=True,blank=True)
    
    
    def __str__(self):
        return f'user {self.user.username}---post {self.caption}'
    
    
    

class LikeDislikeModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'likeuser')
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE,null=True,blank=True)
    like = models.IntegerField(default=0,null=True,blank=True)
    dislike = models.IntegerField(default=0,null=True,blank=True)
    like_permi = models.BooleanField(default=False,null=True,blank=True)
    dislike_permi = models.BooleanField(default=False,null=True,blank=True)
    
    
    
    def __str__(self):
        return f'user {self.user.username}-----post {self.post_id}'
    

    

class UserAddress(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,related_name='address')
    phone_number = models.CharField(max_length=12,null=True, blank=True)
    location = models.CharField(max_length=200)
    
    
    def __str__(self):
        return f'{self.user.username}'
    
 
 
 
    
class Comment(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # j somoy ei class er object creae hobe thikon current time ta rekhe dibe
    
    def __str__(self):
        return f'coomment by {self.name}'
    

    
    
    
    