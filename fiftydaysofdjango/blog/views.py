from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.views.generic import ListView




def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        "blog/post/list.html",
        {'posts' : posts}
    )

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status= Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day)
    return render(
        request, 
        'blog/post/detail.html', 
        {'post': post}
    )

class PostListView(ListView):
    """
    Primera prueba de vista en forma de clases
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/post/list.html'