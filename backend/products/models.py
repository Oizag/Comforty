from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название категории",
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Slug категории",
        db_index=True,
    )
    order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["order", "name"]
        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["order"]),
        ]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("products:category_detail", kwargs={"slug": self.slug})


class Product(models.Model):
    class Badge(models.TextChoices):
        NONE = "", "None"
        NEW = "new", "New"
        SALE = "sale", "Sale"
        FEATURED = "featired", "Featured"

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products", db_index=True, verbose_name="Категория"
    )
    name = models.CharField(max_length=200, verbose_name="Название продукта")
    slug = models.SlugField(max_length=220, unique=True, db_index=True)
    sku = models.CharField(max_length=100, blank=True, default="")
    description = models.TextField(blank=True, default="", verbose_name="Описание")

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    old_proce = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Старая цена")
    currency = models.CharField(max_length=3, default="RUB", verbose_name="Валюта")

    in_stock = models.BooleanField(default=True, verbose_name="В наличии")
    stock_qty = models.PositiveIntegerField(default=0, verbose_name="Количество на складе")

    badge = models.CharField(
        max_length=10, choices=Badge.choices, default=Badge.NONE, db_index=True, verbose_name="Бренд"
    )

    rating_abg = models.FloatField(default=0.0, verbose_name="Рейтинг")
    rating_count = models.PositiveIntegerField(default=0, verbose_name="Количество оценок")

    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["category"]),
            models.Index(fields=["price"]),
            models.Index(fields=["-created_at"]),
            models.Index(fields=["badge"]),
        ]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.slug})


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_images",
        verbose_name="Карточка товара",
        db_index=True,
    )
    image = models.ImageField(
        upload_to="products/%Y/%m/",
        verbose_name="Изображение товара",
    )

    is_primary = models.BooleanField(default=False, verbose_name="Основное изображение")
    sort_order = models.PositiveIntegerField(default=0, verbose_name="Порядок сортировки")

    class Meta:
        ordering = ["id"]
        indexes = [
            models.Index(fields=["product"]),
            models.Index(fields=["is_primary", "sort_order"]),
        ]
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"

    def __str__(self) -> str:
        return f"{self.product.name} ({'primary' if self.is_primary else 'extra'})"
