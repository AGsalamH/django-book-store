from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class RegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone", "country", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.base_fields:
            self.base_fields[field].widget.attrs.update({
                'class': 'form-control'
            })

            if self.base_fields[field].required:
                self.base_fields[field].label_suffix = ' *'
            else:
                self.base_fields[field].label_suffix = ''



class LoginForm(forms.Form):
    error_messages = {
        'invalid_login': _(
            "Please enter a correct email and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

    email = forms.EmailField(max_length=255, widget= forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.request = request

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(self.error_messages['invalid_login'])
        return email

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user = authenticate(self.request, email=email, password=password)
        if user is None:
            raise forms.ValidationError(self.error_messages['invalid_login'])
        self.confirm_login_allowed()
        self.user = user
        return cleaned_data

    def confirm_login_allowed(self):
        if not self.user.is_active:
            raise forms.ValidationError(self.error_messages['inactive'])

    def get_user(self):
        return self.user
