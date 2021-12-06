from django.test import TestCase
from django.urls import reverse

class ThingTests(TestCase):

    def test_wrong_url_returns_404(self):
        response = self.client.get('snack_list.html')
        self.assertEqual(response.status_code, 404)

    def test_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_base_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "_base.html")

    def test_list_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")


    def test_list_page_and_base_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "_base.html")