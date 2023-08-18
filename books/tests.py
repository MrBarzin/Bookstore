from django.test import TestCase,Client
from django.urls import reverse
from .models import Book,Review
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission,User
from accounts.models import CustomUser

class BookTest(TestCase):
           
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username = 'reviewer',
            email = 'reviewer@example.com',
            password = 'reviewer1234',
        )
        
        self.special_permission = Permission.objects.get(
            codename='special_status'
        )
    
        self.book = Book.objects.create(
            title= 'examplebook',
            author = 'exampleauthor', 
            price = '90.00',
        )
        self.review = Review.objects.create(
            book = self.book,
            username = self.user,
            reviewTitle = 'exampletitle',
            reviewText = 'exampletext',
        )

    def test_book_listing(self):
        self.assertEqual(str(self.book.title), 'examplebook')
        self.assertEqual(str(self.book.author), 'exampleauthor')
        self.assertEqual(str(self.book.price), '90.00')

    def test_book_list_view_for_logged_in(self):
        self.client.login(email='reviewer@example.com',password='reviewer1234')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'examplebook')
        self.assertTemplateUsed(response,'books/book_list.html')
    
    def test_book_list_view_for_logged_out(self):
        self.client.logout()
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
        response, '%s?next=/books/' % (reverse('account_login')))
        response = self.client.get('%s?next=/books/' % (reverse('account_login')))
        self.assertContains(response, 'login')


    def test_book_detail_view_with_permission(self):
        self.client.login(email='reviewer@example.com',password='reviewer1234')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url() )
        no_response = self.client.get('books/1234/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'examplebook')
        self.assertContains(response,'exampletitle')
        self.assertTemplateUsed(response, 'books/book_detail.html')