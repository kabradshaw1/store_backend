from importlib import import_module
from user.models import User
from store.models import Category, Order, OrderedItem, Item
from django.conf import settings
from django.test.runner import DiscoverRunner


class BackendTestRunner(DiscoverRunner):
  def setup_test_environment(self, **kwargs):
    """We set the TESTING setting to True. By default, it's on False."""
    super().setup_test_environment(**kwargs)
    settings.TESTING = True

  def setup_databases(self, **kwargs):
    """We set the database"""
    r = super().setup_databases(**kwargs)
    self.user = User.objects.create_user(username="testuser@example.com", password="12345678", email="testuser@example.com")
    self.category = Category.objects.create(name='Food')
    self.item = Item.objects.create(name='stuff', price='1', image='test.jpg', slug='test', description='test test test', quantity=200, category_id=1,)
    self.order = Order.objects.create(user_id=1, price='1')
    self.ordereditem = OrderedItem.objects.create(item_id=1, order_id=1, cartQty=1, price="1")
    return r

  @classmethod
  def load_fixtures(cls):
    try:
      module = import_module(f"core.fixtures")
      getattr(module, "run_fixtures")()
    except ImportError:
      return