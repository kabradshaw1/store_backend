"""
Tests for models.
"""
from django.test import TestCase

from user.models import User
from store import models

def create_user(username='testuser', email='user@example.com', password='testpass123'):
  """Create and return a new user."""
  return User.objects.create_user(username, email, password)

class ModelTests(TestCase):
  """Test models."""

  def test_creating_category(self):
    """Test creating a category is successful."""
    category = models.Category.objects.create(name='test')

    self.assertEqual(str(category), category.name)

  def test_create_order(self):
    """Test creating an order is successful."""
    user = User.objects.create_user(
      'test@example.com',
      'testpass123',
    )
    order = models.Order.objects.create(
      user=user,
      price='5.00'
    )

    self.assertEqual(int(order), order.id)

  def test_create_item(self):
    """Test creating an item is successful"""
    models.Category.objects.create(name='test')
    item = models.Item.objects.create(
      name='test',
      price='1.00',
      category=1,
      image='test.jpg',
      slug='test',
      description='test',
      quanitity=1,
    )

    self.assertEqual(str(item), item.name)

  def test_create_ordered_item(self):
    """Test creating an ordered item is successful."""
    user = User.objects.create_user(
      'test@example.com',
      'testpass123',
    )
    models.Item.objects.create(
      name='test',
      price='1.00',
      category=1,
      image='test.jpg',
      slug='test',
      description='test',
      quanitity=1,
    )
    models.Order.objects.create(
      user=user,
      price='5.00'
    )
    ordered_item = models.OrderedItem.objects.create(
      order=1,
      item=1,
      cartQty=1,
      price='1.00'
    )
    self.assertEqual(str(int(ordered_item)), ordered_item.id)