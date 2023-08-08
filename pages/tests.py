from django.test import SimpleTestCase
from django.urls import reverse,resolve
from .views import HomePage

class HomePageTestCase(SimpleTestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_home_page_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'homepage.html')

    def test_home_page_contain_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response,'homepage')
    
    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response,'anything')
    
    def test_home_page_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePage.as_view().__name__)
