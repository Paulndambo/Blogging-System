from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from . forms import SignupForm, EditProfileForm, PasswordChangingForm, ProfileCreateForm
from data.models import Profile
# Create your views here.
class CreateProfile(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = "registration/create_profile.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    fields = ['bio', 'profile_pic', 'website', 'facebook', 'twitter', 'linkedin']
    template_name = 'registration/edit_user_profile.html'
    success_url = reverse_lazy('home')

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs): 
        context = super(ShowProfilePageView,
                        self).get_context_data(*args, **kwargs)

        current_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['current_user'] = current_user
        return context

class UserRegisterView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    #form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, "registration/password_success.html")
