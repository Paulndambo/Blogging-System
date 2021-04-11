from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from data.models import Profile

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website', 'facebook',
                  'twitter', 'instagram', 'linkedin')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            #'profile_pic': forms.ImageField(),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    username = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    last_login = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_joined = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(
        max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(
        max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
