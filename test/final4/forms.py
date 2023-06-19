from .models import Sale
from django import forms


# Model Form
class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('count',) # 이 필드를 파이썬 클래스화