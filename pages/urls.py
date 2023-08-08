from django.urls import include,path
from pages.views import HomePage

urlpatterns =[
    path('', HomePage.as_view(),name='home'),
]