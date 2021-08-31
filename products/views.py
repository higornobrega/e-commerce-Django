from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Category, Product


class ProductDetailView(DetailView):
    queryset = Product.available.all()


class ProductListView(ListView):
    category = None
    paginate_by = 6

    def get_queryset(self):
        queryset = Product.available.all()

        category_slug = self.kwargs.get("slug")
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = Category.objects.all()
        return context


'''
class ProductListView(ListView):
    category = None
    paginate_by = 6
    # Listar de 6 em 6 produtos

    def get_queryset(self):
        # Reescrevendo o método 

        queryset = Product.available.all()
        # queryset é todos os produtos disponíveis

        category_slug = self.kwargs.get("slug")
        # category_slug -> Se vier um slug coloca em category_slug

        if category_slug:
            # Se veio slug entra
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)
            # Pegar todos os produtos dessa categoria

        return queryset

    def get_context_data(self, **kwargs):
        # Reescrevendo o método 
        context = super().get_context_data(**kwargs)
        # Pega tudo disponível
        context["category"] = self.category
        #   * Mais category
        context["categories"] = Category.objects.all()
        #   *Mais categories
        return context
        '''