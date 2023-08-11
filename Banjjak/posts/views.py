from rest_framework import viewsets
from .models import Post
from .serializers import PostListSerializer

# from django.shortcuts import render, redirect
# from .forms import PostForm

# def posts_index(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save()  # 폼 데이터를 데이터베이스에 저장
#             # Assuming 'tags' is submitted in the form
#             tags = request.POST.get('tags')
#             post.tags.set(tags.split(','))  # Set the tags
#             # return redirect('posts:index')  # 작성 후에 리스트 페이지로 리디렉션
#     else:
#         form = PostForm()
#     return render(request, "manager_post.html", {'form': form})

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer