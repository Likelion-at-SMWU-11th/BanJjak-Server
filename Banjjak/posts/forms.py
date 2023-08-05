from django import forms
from .models import Post  # Post 모델 임포트

class PostForm(forms.ModelForm):  # 모델 폼으로 정의
    class Meta:
        model = Post
        fields = '__all__'  # 혹은 원하는 필드를 지정
