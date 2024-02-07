from django.urls import path,include
from .import views

urlpatterns = [
    path('like/<int:id>/<int:user_id>/',views.likeview,name='like'),
    path('dislike/<int:id>/<int:user_id>/',views.dislikeview,name='dislike'),
    path('dashboard/',views.dashboardview,name='dashboard'),
    path('user_post/<int:user_id>/',views.user_post,name='userPost'),
    
    
    
    path('add_post/',views.addpostview,name='addPost'),
    
    
    
    path('detailview/<int:pk>/', views.DetailViewOfPost.as_view(), name='detailview'),
    path('edit/<int:id>',views.edit_post,name='editpost'),
    path('delete/<int:id>',views.delete_post,name='deletepost'),
    path('editComment/<int:id>/<int:post_id>/',views.edit_comment,name='editcomment'),
    path('deleteComment/<int:id>/<int:post_id>/',views.delete_comment,name='deletecomment'),
    path('allLikeUser/<int:post_id>',views.alluserviewoflike,name='allLikeUser'),
    path('allDislikeUser/<int:post_id>',views.alluserviewofdislike,name='allDislikeUser'),
    path('userview/<int:user_id>',views.viewofuserlikedislike,name='userview')
]
