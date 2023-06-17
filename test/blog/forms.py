from .models import Comment
from django import forms


# Model Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',) # 이 필드를 파이썬 클래스화