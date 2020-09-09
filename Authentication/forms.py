from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

class CreateUserForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'