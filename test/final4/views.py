from django.shortcuts import render
from django.views.generic import ListView, DetailView # CBV
from .models import Product,Sale #모델 사용
from .forms import SaleForm
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect # FBV




# Create your views here.
def index(request):
    return render(
        request,
        'final4/index.html',
    )



class ProductList(ListView):
    model = Product
    ordering = '-pk'
    paginate_by = 3
    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data()
        return context

    template_name = 'final4/product_list.html'


class ProductDetail(DetailView):
    model = Product
    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        context['sale_form'] = SaleForm
        return context

    template_name = 'final4/product_detail.html'


def buyProduct(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk) # 객체 확인

        # post 형식이면 파이썬 형식으로 form 만들고 저장
        if request.method == 'POST':
            sale_form = SaleForm(request.POST)
            if sale_form.is_valid():
                sale = sale_form.save(commit=False)
                sale.product = product
                sale.user = request.user
                sale.save()
                return redirect(product.get_absolute_url()) # 작성 후 댓글 링크
        else:
            return redirect(product.get_absolute_url()) # get이면 그냥 detail링크

    else:
        raise PermissionDenied


class CartList(ListView):
    model = Sale
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(CartList, self).get_context_data()
        context['sale_list'] = Sale.objects.filter(user=self.request.user)
        return context

    template_name = 'final4/sale_list.html'