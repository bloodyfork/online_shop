from django.views import generic
from product.models import Product, Category


class StoreListView(generic.ListView):
    model = Product
    template_name = "product/store.html"
    context_object_name = 'products'


class CategoryListView(generic.ListView):
    model = Category
    template_name = "product/categories.html"
    context_object_name = 'category'


class CategoryBasedProductListView(generic.ListView):
    model = Product
    template_name = "product/categorybasedproduct.html"
    context_object_name = 'products'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        query = Product.objects.filter(category__base_category__name=slug)
        return query

    # def get(self, request, *args, **kwargs):
    #     # slug = kwargs['slug']
    #     kwargs['context']['products'] = Product.objects.filter(category__base_category__name=kwargs['slug'])
    #     return super().get(request, *args, **kwargs)


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "product/ProductDetail.html"
    context_object_name = "product"
    pk_url_kwarg = "pk"
