from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Category(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:list_by_category", kwargs={"slug": self.slug})


class Product(TimeStampedModel):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})





'''from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
# TimeStampedModel cria dois campos extra
    #   *Created -> Data de criação
    #   *Morefind -> Quando foi modificado

class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)
        # Pega o objects (queryset padão) com um filtro para retornar apenas os products disponíveis


class Category(TimeStampedModel):
    # TimeStampedModel cria dois campos extra
    #   *Created -> Data de criação
    #   *Morefind -> Quando foi modificado
    name = models.CharField(max_length=255, unique=True)
    # unique=True -> Será único
    # always_update=False -> slug não vai mudar se o nome mudar
    # populate_from="name" -> Será populado a partir de nome
    #   * Ao adicionar um name o slug é gerado automaticamente a partir do name
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name") 

    class Meta:
        ordering = ("name",)
        # Ordenação por name de A a Z
        verbose_name = "category"
        # Como vai ser escrito no singular na pagina 
        verbose_name_plural = "categories"
        # Como vai ser inscrito no plural na página

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Pega a url absoluta
        return reverse("products:list_by_category", kwargs={"slug": self.slug})


class Product(TimeStampedModel):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    # related_name="products" -> Para ter acesso a todos os produtos dessa categoria com o (.products)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    # ImageField -> Para guardar imagens
    # upload_to="products/%Y/%m/%d" -> Vai carregar a imagem dentro de mídia, a pasta de products, colocando o ano, mês e dia do upload
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})
'''