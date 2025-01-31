from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from .models import Subscriber
from .forms import PostForm
from user_profile.models import UserProfile


# Create your views here.

class PostList(generic.ListView):
    """
    View to display a paginated list of published blog posts.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog_list.html'
    paginate_by = 6


def home(request):
    """
    View to display the homepage with featured blog posts.
    """
    featured_posts = Post.get_featured_posts()
    return render(request, 'index.html', {'featured_posts': featured_posts})


def post_detail(request, slug):
    """
    Display an individual blog post along with its comments.
    Handles visibility based on user role (author, superuser, or regular user).
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    
    # Check if user can view the post (author, superuser, or approved post)
    is_author = request.user == post.author
    is_superuser = request.user.is_superuser
    is_published = post.status == 1 and post.approved

    # If user is not author or superuser, and post isn't published, redirect
    if not (is_author or is_superuser or is_published):
        messages.info(request, 'This post is awaiting approval.')
        return redirect('home')

    # Get approved comments for regular users, all comments for author/superuser
    if is_author or is_superuser:
        comments = post.comments.all().order_by("-created_on")
    else:
        comments = post.comments.filter(approved=True).order_by("-created_on")
    
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, 'Please log in to comment.')
            return redirect('login')
            
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval.')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    context = {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "is_author": is_author,
        "is_superuser": is_superuser
    }

    return render(request, "blog/post_detail.html", context)


def comment_edit(request, slug, comment_id):
    """
    View to edit comments
    """
    post = get_object_or_404(Post, status=1, slug=slug)  # Ensure status is checked
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author != request.user:
        messages.error(request, "You can only edit your own comments!")
        return redirect('post_detail', slug=slug)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            updated_comment = comment_form.save(commit=False)
            updated_comment.approved = False
            updated_comment.save()
            messages.success(request, 'Comment updated and awaiting approval!')
            return redirect('post_detail', slug=slug)
        else:
            messages.error(request, 'Error updating comment!')
    else:
        comment_form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {
        'comment_form': comment_form,
        'post': post,
        'comment': comment
    })


def comment_delete(request, slug, comment_id):
    """
    View to delete comment.
    """
    post = get_object_or_404(Post, status=1, slug=slug)  # Ensure status is checked
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Comment deleted!'
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own comments!'
        )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def subscribe(request):
    """
    View to handle email subscriptions.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if not Subscriber.objects.filter(email=email).exists():
                Subscriber.objects.create(email=email)
                messages.success(request, 'Thank you for subscribing!')
                return render(request, 'subscribe_success.html')
            else:
                messages.info(request, 'You are already subscribed.')
        else:
            messages.error(request, 'Please provide a valid email address.')
    return redirect('home')


def user_profile_view(request, username):
    """
    View to display a user's public profile by their username.
    """
    user_profile = get_object_or_404(UserProfile, user__username=username)

    return render(
        request,
        'user_profile/view_user_profile.html',
        {'user_profile': user_profile}
    )


def create_post(request):
    """
    View to handle the creation of a new blog post by the user.
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.status = 2  # Adjust status as needed
            post.save()
            messages.success(request, 'Your post is awaiting approval.')
            return redirect('user_profile')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


@login_required
def edit_post(request, post_id):
    """
    View to edit an existing blog post by the author.
    """
    post = get_object_or_404(Post, id=post_id)

    # Check if the logged-in user is the author of the post
    if post.author != request.user:
        messages.error(request, "You are not allowed to edit this post.")
        return redirect('post_detail', slug=post.slug)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated successfully.')
            return redirect('user_profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


def delete_post(request, post_id):
    """
    View to delete an existing blog post by the author.
    """
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted successfully.')
        return redirect(
            reverse(
                'user_profile',
                kwargs={'username': request.user.username}
            )
        )

    return render(
        request,
        'blog/post_confirm_delete.html',
        {'post': post}
    )
