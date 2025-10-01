from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nome_completo = forms.CharField(max_length=100, required=True)
    matricula = forms.CharField(max_length=20, required=True)
    telefone = forms.CharField(max_length=15, required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'nome_completo', 'matricula', 'telefone', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.nome_completo = self.cleaned_data['nome_completo']
        user.matricula = self.cleaned_data['matricula']
        user.telefone = self.cleaned_data['telefone']
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('nome_completo', 'email', 'telefone', 'data_nascimento', 'endereco', 'foto_perfil')
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'endereco': forms.Textarea(attrs={'rows': 3}),
        }