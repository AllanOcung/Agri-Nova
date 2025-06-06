from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import FarmerProfile, Farm

class FarmerRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(required=False)
    role = forms.ChoiceField(choices=FarmerProfile.USER_ROLES, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            FarmerProfile.objects.create(
                user=user,
                phone=self.cleaned_data.get('phone', ''),
                role=self.cleaned_data.get('role', 'farmer')
            )
        return user

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['location', 'crops']
        


class FarmerLoginForm(AuthenticationForm):
    username = forms.CharField(label="Email or Username")
    password = forms.CharField(widget=forms.PasswordInput)