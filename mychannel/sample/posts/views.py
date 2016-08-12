from django.db.models import Max
from django.shortcuts import render, get_object_or_404
from .models import Blog


def index(request):
    """
    Root page view. Just shows a list of liveblogs.
    """
    # Get a list of liveblogs, ordered by the date of their most recent
    # post, descending (so ones with stuff happening are at the top)
    blogs = Blog.objects.annotate(
        max_created=Max("posts__created")
    ).order_by("-max_created")

    # Render that in the index template
    return render(request, "posts/index.html", {
        "blogs": blogs,
    })


def my_blog(request, slug):
    """
    Shows an individual liveblog page.
    """
    # Get the liveblog by slug
    blog = get_object_or_404(Blog, slug=slug)

    # Render it with the posts ordered in descending order.
    # If the user has JavaScript enabled, the template has JS that will
    # keep it updated.
    return render(request, "posts/blog.html", {
        "blog": blog,
        "posts": blog.posts.order_by("-created"),
})