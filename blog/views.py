from django.shortcuts import render
from django.utils import timezone

# the . before models current directory
from .models import Post



# Create your views here.
def post_list(request):
    # posts is the name of the query set
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

