from django.urls import include,path
from pages.views import HomePage,AboutPage

urlpatterns =[
    path('', HomePage.as_view(),name='home'),
    path('about/', AboutPage.as_view(),name='about'),
]