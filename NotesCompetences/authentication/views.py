from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.views.generic import View, FormView, RedirectView
from django.contrib.auth import views as auth_views
from .forms import SignUpForm

# Create your views here.
def profileView(request):
	return render(request, 'authentication/profile.html')


# NOT USED
class GuestOnlyView(View):
    def dispatch(self, request, *args, **kwargs):
        # Redirect to the index page if the user already authenticated
        if request.user.is_authenticated:
            return redirect('gestion:classe_list')

        return super().dispatch(request, *args, **kwargs)


class UserSignUpView(GuestOnlyView, FormView):
	form_class = SignUpForm
	template_name = 'authentication/sign-up.html'

	def form_valid(self, form):
		user = form.save(commit=False)

        #user.username = form.cleaned_data.get('username')

        # Create a user record
		user.save()
		raw_password = form.cleaned_data.get('password')

		user = authenticate(username=user.username, password=raw_password)
		if user is not None:
			login(self.request, user)

		return super().form_valid(form)

	def get_success_url(self):
		return reverse('gestion:classe_list')

class UserSignInView(GuestOnlyView, FormView):
	pass