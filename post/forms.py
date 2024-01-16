from typing import Any
from django import forms
from .import models



class AddPostForm(forms.ModelForm):
    class Meta:
        model = models.PostModel
        fields = ['user','caption','body','post_image']
        
    # def save(self, commit=False):
    #     current_user = super().save(commit=True)
    #     post = None
        
    #     if commit:
    #         current_user.save()
    #         post = models.PostModel.objects.create(
    #             user = current_user,
    #         )
    #         models.PostModel.save()
    #     return post
    
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name','email','body']
        


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = models.PostModel
        fields = ['caption','body']    
        
        

            
        
