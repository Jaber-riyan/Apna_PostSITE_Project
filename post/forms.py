from typing import Any
from django import forms
from .import models



class AddPostForm(forms.ModelForm):
    class Meta:
        model = models.PostModel
        fields = ['caption','body','post_image']
    
    
    
    
    
    
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name','email','body']
        


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = models.PostModel
        fields = ['caption','body']    
        
        

            
        
