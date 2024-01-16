from django.contrib import admin
from .import models
# Register your models here.


admin.site.register(models.UserAddress)
admin.site.register(models.PostModel)
admin.site.register(models.Comment)
admin.site.register(models.LikeDislikeModel)


