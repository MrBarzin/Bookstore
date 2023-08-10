from django.test import SimpleTestCase,TestCase
from django.urls import reverse,resolve
from .views import HomePage,AboutPage

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
        
class AboutPageTest(TestCase):

    def setUp(self) :
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code,200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response,'about.html')
    
    def test_aboutpage_contain_correct_html(self):
        self.assertContains(self.response,"About Page")

    def test_aboutpage_DoesNot_contains_correct_html(self):
        self.assertNotContains(self.response,'Hi there! I should not be in this page')

    def test_aboutPage_url_resolve_aboutpageTemplate(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__,AboutPage.as_view().__name__)
