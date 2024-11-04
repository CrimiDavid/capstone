from django.test import TestCase
from restaurant.models import Menu


class MenuItemsViews(TestCase):
    def setUp(self):
        shakshuka = Menu.objects.create(dish='sadsada', price=8.50, inventory=10)
        Hummus = Menu.objects.create(dish='dsadas', price=5.00, inventory=20)

    def test_menu_items_list(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'sadsada')
        self.assertContains(response, 'dsadas')