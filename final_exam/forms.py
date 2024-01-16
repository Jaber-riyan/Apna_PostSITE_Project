from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from post.models import UserAddress


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    phone_number = forms.CharField(max_length=12)
    location = forms.CharField(max_length=200)
    user_image = forms.ImageField()
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','phone_number','location',]
        model.is_active = False
        
    def save(self,commit=True):
        our_user = super().save(commit=False)
        if commit== True:
            our_user.is_active = False
            our_user.save()
            phone_number = self.cleaned_data.get('phone_number')
            location = self.cleaned_data.get('location')
            
            UserAddress.objects.create(
                user = our_user,
                phone_number = phone_number,
                location = location,
            )
        return our_user
    
    

class UserUpdateForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=12)
    location = forms.CharField(max_length=200)
    
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        if self.instance:
            try:
                user_address = self.instance.address
            except UserAddress.DoesNotExist:
                user_address = None

            if user_address:
                self.fields['phone_number'].initial = user_address.phone_number
                self.fields['location'].initial = user_address.location
    
    
    
    def save(self, commit=True):
        user = super().save(commit=False)
        
        if commit:
            user.save()
            
            user_address, created = UserAddress.objects.get_or_create(user=user)
            
            
            user_address.phone_number = self.cleaned_data['phone_number']
            user_address.location = self.cleaned_data['location']
            user_address.save()
        return user
        
    
    
    
    