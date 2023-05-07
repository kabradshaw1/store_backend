"""
Tests for user models.
"""
from django.test import TestCase

from user.models import User

class ModelTests(TestCase):
  """Test user models."""

  def test_create_user_with_email_successful(self):
    """Test creating a user with an email is successful."""
    email = 'test@example.com'
    password = 'testpass123'
    user = User.objects.create_user(
      username=email,
      email=email,
      password=password,
    )

    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))

