
from django.urls import path

from .views import ProductDetailView, ProductListView

app_name = "products"

urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    path("category/<slug:slug>/", ProductListView.as_view(), name="list_by_category"),
]



'''from django.urls import path

from .views import ProductDetailView, ProductListView

app_name = "products"

urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    # Lista todos os produtos
    path("<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    # Se enviar um slug msotra as informações de um produto
    path("category/<slug:slug>/", ProductListView.as_view(), name="list_by_category")
    # Lista por categoria
]
'''