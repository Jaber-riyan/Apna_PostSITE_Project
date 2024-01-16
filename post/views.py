from django.shortcuts import render, redirect
from .models import PostModel, LikeDislikeModel, Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import AddPostForm, CommentForm, PostUpdateForm
from django.contrib import messages
from django.views.generic import DetailView






@login_required
def likeview(request,id,user_id):
    
    post_cl = PostModel.objects.get(id=id)
    login_user = User.objects.get(id=request.user.id)
    if LikeDislikeModel.objects.filter(post=post_cl,user=login_user).exists():
        
        
        isExist = LikeDislikeModel.objects.get(post=post_cl,user=login_user)
        
        if isExist.like_permi == True:
            messages.info(request,'You Already Like this post')
            return redirect('homepage')
        
        else: 
            messages.info(request,'You Already Dislike this post')
            return redirect('homepage')
    
    
        
    else:
        noObject = LikeDislikeModel.objects.create(
            user = login_user,
            post = post_cl,
            like = 1,
            like_permi = True
        )
        noObject.save()
        return redirect('homepage')
        




@login_required
def dislikeview(request,id,user_id):
    post_cl = PostModel.objects.get(id=id)
    login_user = User.objects.get(id=request.user.id)
    if LikeDislikeModel.objects.filter(post=post_cl,user=login_user).exists():
        
        
        isExist = LikeDislikeModel.objects.get(post=post_cl,user=login_user)
        
        if isExist.dislike_permi == True:
            messages.info(request,'You Already Dislike this post')
            return redirect('homepage')
        
        else: 
            messages.info(request,'You Already Like this post')
            return redirect('homepage')
    
    
        
    else:
        noObject = LikeDislikeModel.objects.create(
            user = login_user,
            post = post_cl,
            dislike = 1,
            dislike_permi = True
        )
        noObject.save()
        return redirect('homepage')


    
    
@login_required
def dashboardview(request):
    return render(request, 'dashboard.html')


def user_post(request,user_id):
    user = User.objects.get(id=user_id)
    data = PostModel.objects.filter(user=user)
    # print(user.username)
    return render(request,'user_post.html',{'posts':data})







@login_required
def addpostview(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST,request.FILES)
        if form.is_valid():
            # caption = form.cleaned_data['caption']
            # print(caption)
            messages.success(request,'Post Added Successfully')
            form.instance.user=request.user
            form.save()
            return redirect('userPost',user_id=request.user.id)
        else:
            print(form.errors)
            messages.error(request,'Nope Make a error when your add post plz solve this error')
    else:
        form = AddPostForm()
    return render(request,'add_post.html',{'form':form,'text':'Add Post'})








class DetailViewOfPost(DetailView):
    model = PostModel
    pk_url_kwarg = 'pk'
    template_name = 'post_detail.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            comment_form.instance.name = request.user.username
            comment_form.instance.email = request.user.email
            messages.success(request,'Comment created Successfully')
            new_comment.save()
        return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = CommentForm()
        # print(self.pk_url_kwarg)

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    
    
def edit_post(request,id):
    post = PostModel.objects.get(pk=id)
    form = PostUpdateForm(instance=post)
    # print(post.name)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'Post updated successfully')
            return redirect('userPost',user_id=post.user.id)
    return render(request, 'add_post.html',{'form': form,'text':'Post Edit'})



def delete_post(request,id):
    delete = PostModel.objects.get(pk=id)
    delete.delete()
    messages.success(request,'Delete post successfully')
    return redirect('userPost',user_id=request.user.id)



def edit_comment(request,id,post_id):
    user = request.user
    # print(user.username)
    post_cl = PostModel.objects.get(id=post_id)
    # print(post_cl.caption)
    if Comment.objects.filter(id=id,name=user.username,email=user.email).exists():
        comment = Comment.objects.get(id=id,name=user.username,email=user.email)
        # print(comment.body)
        # return redirect('homepage')
        # comment = Comment.objects.get(pk=id)
        form = CommentForm(instance=comment)
        # print(post.name)
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                messages.success(request,'Comment updated successfully')
                return redirect('detailview',pk=post_cl.id)
        else:
            form = CommentForm(instance=comment)
        return render(request, 'update_comment.html',{'form': form,'text':'Comment Edit'})
    
     
    
    else:
        messages.error(request,'You Can not edit another user comment')
        return redirect('detailview',pk=post_cl.id)
    
    
    
    
def delete_comment(request,id,post_id):
    user = request.user
    print(user.username)
    post_cl = PostModel.objects.get(id=post_id)
    print(post_cl.caption)
    if Comment.objects.filter(id=id,name=user.username,email=user.email).exists():
        comment = Comment.objects.get(id=id,name=user.username,email=user.email)
        comment.delete()
        messages.success(request,'Comment Deleted Successfully')
        return redirect('detailview',pk=post_cl.id)
    
    
    
    
    else:
        messages.error(request,'You Can not Delete another user comment')
        return redirect('detailview',pk=post_cl.id)
