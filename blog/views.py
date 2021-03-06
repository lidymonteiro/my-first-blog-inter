from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import PostPt, PostEn, PostEs
from .forms import PostFormPt, PostFormEn, PostFormEs

"""
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
"""

def post_list(request):
    language = request.LANGUAGE_CODE
    if language == 'pt-br':
        posts = PostPt.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    elif language == 'en':
        posts = PostEn.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    elif language == 'es':
        posts = PostEs.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

"""
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
"""

def post_detail_pt(request, pk):
    post = get_object_or_404(PostPt, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_detail_en(request, pk):
    post = get_object_or_404(PostEn, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_detail_es(request, pk):
    post = get_object_or_404(PostEs, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    language = request.LANGUAGE_CODE

    if request.method == 'POST':
        if language == 'pt-br':
            form = PostFormPt(request.POST)
            language = 'pt'
        elif language == 'en':
            form = PostFormEn(request.POST)
        elif language == 'es':
            form = PostFormEs(request.POST)
        #form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail_'+language, pk=post.pk)
    else:
        if language == 'pt-br':
            form = PostFormPt()
        elif language == 'en':
            form = PostFormEn()
        elif language == 'es':
            form = PostFormEs()
        #form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    language = request.LANGUAGE_CODE
    if language == 'pt-br':
        post = get_object_or_404(PostPt, pk=pk)
    elif language == 'en':
        post = get_object_or_404(PostEn, pk=pk)
    elif language == 'es':
        post = get_object_or_404(PostEs, pk=pk)
    #post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        if language == 'pt-br':
            form = PostFormPt(request.POST, instance=post)
            language = 'pt'
        elif language == 'en':
            form = PostFormEn(request.POST, instance=post)
        elif language == 'es':
            form = PostFormEs(request.POST, instance=post)
        #form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail_'+language, pk=post.pk)
    else:
        if language == 'pt-br':
            form = PostFormPt(instance=post)
        elif language == 'en':
            form = PostFormEn(instance=post)
        elif language == 'es':
            form = PostFormEs(instance=post)
        #form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    language = request.LANGUAGE_CODE
    if language == 'pt-br':
        Post = PostPt
    elif language == 'en':
        Post = PostEn
    elif language == 'es':
        Post = PostEs
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    language = request.LANGUAGE_CODE
    if language == 'pt-br':
        Post = PostPt
        language = 'pt'
    elif language == 'en':
        Post = PostEn
    elif language == 'es':
        Post = PostEs
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail_'+language, pk=pk)

@login_required
def post_remove(request, pk):
    language = request.LANGUAGE_CODE
    if language == 'pt-br':
        Post = PostPt
        language = 'pt'
    elif language == 'en':
        Post = PostEn
    elif language == 'es':
        Post = PostEs
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')