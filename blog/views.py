from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
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
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    comments = post.comments.all().order_by("-created_on")

    comment_count = post.comments.filter(approved=True).count()

    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval.'
            )

            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    View to edit comments
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
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
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
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
            post.status = 2
            post.save()
            messages.success(request, 'Your post is awaiting approval.')
            return redirect('user_profile')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


def edit_post(request, post_id):
    """
    View to edit an existing blog post by the author.
    """
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your post has been updated successfully.'
            )
            return redirect('user_profile')
        else:
            messages.error(
                request,
                'Please correct the errors below.'
            )
    else:
        form = PostForm(instance=post)

    return render(
        request,
        'blog/edit_post.html',
        {'form': form, 'post': post}
    )


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
                'user_profile',  # Make sure this matches your URL configuration
                kwargs={'username': request.user.username}  # Ensure this username is correct
            )
        )

    return render(
        request,
        'blog/post_confirm_delete.html',
        {'post': post}
    )
