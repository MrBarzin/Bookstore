from django.test import TestCase
from django.urls import reverse
from .models import Book,Review
from django.contrib.auth import get_user_model


class BookTest(TestCase):
           
    def setUp(self):
        self.user = get_user_model().objects.create(
            username = 'reviewer',
            email = 'reviewer@example.com',
            password = 'reviewer1234',
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

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'examplebook')
        self.assertTemplateUsed(response,'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url() )
        no_response = self.client.get('books/1234/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'examplebook')
        self.assertContains(response,'exampletitle')
        self.assertTemplateUsed(response, 'books/book_detail.html')