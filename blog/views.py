from django.shortcuts import render , get_object_or_404 ,render_to_response
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def post_list(request):
    posts	=	Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request , 'blog/post_list.html',{'posts' : posts})

def post_detail(request , pk):
    post = get_object_or_404(Post , pk=pk)
    return render(request , 'blog/post_detail.html' , {'post':post	})

def post_new(request):
    if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                    post = form.save(commit=False)
                    post.author = request.user
                    post.published_date = timezone.now()
                    post.save()
                    return redirect('blog.views.post_detail' , pk=post.pk)
    else:
        form = PostForm()
        return render(request , 'blog/post_edit.html' , {'form' : form})


def post_edit(request , pk):
    post = get_object_or_404(Post , pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST , instance=post)
        if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('blog.views.post_detail' , pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request , 'blog/post_edit.html' , {'form' : form})

def about_us(request):
    return render(request , 'blog/aboutus.html')

def contact_us(request):
    return render(request , 'blog/contactus.html')

def courses(request):
    return render(request , 'blog/courses.html')





def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def index(request):
    return render_to_response('myapp/index.html')
