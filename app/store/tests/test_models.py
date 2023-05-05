"""
Tests for models.
"""
from unittest.mock import patch
from decimal import Decimal

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
    user = User.objects.create_user(
      'test@example.com',
      'testpass123',
    )

  def test_create_order(self):
    """Test creating an order is successful."""
    pass