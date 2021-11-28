from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField('Название категории', max_length=25)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Brands(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название брэнд')

    class Meta:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)

    name = models.CharField('Название товара', max_length=35)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)

    slug = models.SlugField(unique=True)
    images = models.ImageField()
    description = models.TextField('Описание')

    def __str__(self):
        return f'Артикул: {self.id}   Название: {self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Specification(models.Model):
    name = models.CharField('Название', max_length=25)
    price = models.PositiveSmallIntegerField('Цена')

    def __str__(self):
        return f'{self.name}  {self.price}₽'

    class Meta:
        verbose_name = 'Спецификация'
        verbose_name_plural = 'Спецификации'


class SpecificationsProduct(models.Model):
    specifications = models.ManyToManyField(Specification, verbose_name="Спецификации", blank=True)
    product = models.ForeignKey(Product, verbose_name="К какому товару относится", on_delete=models.CASCADE)

    def __str__(self):
        return f'ID: {self.id}'

    class Meta:
        verbose_name = 'Спецификация для продукта'
        verbose_name_plural = 'Спецификации для продукта'


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Владелец корзины', on_delete=models.CASCADE)
    products = models.ManyToManyField('CartProduct', blank=True, related_name='ProductInCart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Итоговая цена')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartProduct(models.Model):
    user = models.ForeignKey("Customer", on_delete=models.CASCADE)
    cart = models.ForeignKey("Cart", verbose_name="Корзина", on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Итоговая цена')

    def __str__(self):
        return f'Продукт в корзине {self.id}'


class Customer(models.Model):
    user = models.OneToOneField(User, verbose_name='Клиент', on_delete=models.CASCADE)
    #   first_name = models.CharField(max_length=20, verbose_name='Имя')
    #   last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=20, verbose_name='Отчество')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')

    country = models.CharField(max_length=255, verbose_name='Страна')
    region = models.CharField(max_length=255, verbose_name='Регион / Область')
    city = models.CharField(max_length=255, verbose_name='Город')
    address = models.CharField(max_length=255, verbose_name='Адресс')

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'
