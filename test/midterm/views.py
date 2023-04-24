from django.shortcuts import render
from .models import Staff #모델 사용
# Create your views here.
def index(request):

    return render(
        request,
        'midterm/index.html',

    )

def list(request):
    staffs = Staff.objects.all().order_by('-pk') # Post 모델값 pk 역순으로 가져옴

    return render(
        request,
        'midterm/list.html',
        {
            'staffs': staffs # posts로 렌더링
        }

    )

def name_card(request, pk):
    staff = Staff.objects.get(pk=pk)

    return render(
        request,
        'midterm/name_card.html',
        {
            'staff': staff
        }
    )

def name_card2(request, pk):
    staff = Staff.objects.get(pk=pk)

    return render(
        request,
        'midterm/name_card2.html',
        {
            'staff': staff
        }
    )

