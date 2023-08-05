from django.shortcuts import render, redirect
from .forms import PostForm

def posts_index(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # 폼 데이터를 데이터베이스에 저장
            #return redirect('posts:index')  # 작성 후에 리스트 페이지로 리디렉션
    else:
        form = PostForm()
    return render(request, "manager_post.html", {'form': form})
