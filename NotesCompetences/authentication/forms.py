from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class SignUpForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'username']

	first_name = forms.CharField(label='Nom', max_length=50, required=True, widget=forms.TextInput(attrs={'autofocus': True}))
	last_name = forms.CharField(label='Prénom', max_length=50, required=True)
	email = forms.EmailField(label='Email', max_length=255, widget=forms.EmailInput(attrs={'placeholder': '@'}))
	password1 = forms.CharField(label="Mot de passe", required=True, widget=forms.PasswordInput)
	password2 = forms.CharField(label="Confirmation du mot de passe", required=True, widget=forms.PasswordInput)

	error_messages = {
        'unique_email': 'Cet email est déjà utilisé',
    }

	def clean(self):
		cleaned_data = super().clean()

		email = cleaned_data.get('email', '').lower()

		num_users = User.objects.filter(email=email).count()
		if num_users > 0:
			self.add_error('email', self.error_messages['unique_email'])