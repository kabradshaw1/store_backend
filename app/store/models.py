from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.manager import Manager

class Category(models.Model):
  id: int
  items: Manager['Item']

  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Item(models.Model):
  id: int
  # orders: models.ManyToManyField['Order', 'OrderedItem']
  category_id: int
  item: Manager['OrderedItem']

  name = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=8, decimal_places=2)
  category = models.ForeignKey(Category, related_name='items', on_delete=models.PROTECT, default=1)
  image = models.CharField(max_length=50)
  slug = models.SlugField(max_length=50, unique_for_date='created')
  description = models.TextField(max_length=600)
  quantity = models.PositiveIntegerField(default=0)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.name}'

class Order(models.Model):
  id: int
  ordered_items: Manager['OrderedItem']
  user_id: int

  items = models.ManyToManyField(Item, related_name='orders', blank=True, through='OrderedItem')
  user = models.ForeignKey(to='user.User', related_name='order', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  price = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(0.01)])
  # stripe_token = models.CharField(max_length=100)

  def __str__(self):
    return f'{self.price}'

class OrderedItem(models.Model):
  id: int
  order_id: int
  item_id: int

  order = models.ForeignKey(Order, related_name='ordered_items', on_delete=models.CASCADE)
  item = models.ForeignKey(Item, related_name='ordered_item', on_delete=models.CASCADE)
  cartQty = models.PositiveIntegerField(default=1)
  price = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(0.01)])

  def __str__(self):
    return f'{self.price}'



