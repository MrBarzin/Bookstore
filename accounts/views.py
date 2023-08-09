from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    model = get_user_model()
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    

# Create your views here.
