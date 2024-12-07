# from django import forms
# from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# from django.contrib.auth.models import User


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(max_length =60 )

#     class Meta:
#        model = User
#        fields = ("first_name","last_name","username","email","password1","password2")


# class AccountUpdateForm(forms.ModelForm):
    
#     class Meta:
#         model = User
#         fields = ("first_name","last_name",'email')

    

    
#     def clean_first_name(self):
#         if self.is_valid():
#             first_name = self.cleaned_data["first_name"]
            
#             return first_name
    
#     def clean_last_name(self):
#         if self.is_valid():
#             last_name = self.cleaned_data["last_name"]
            
#             return last_name
    

#     def clean_email(self):
#         if self.is_valid():
#             email = self.cleaned_data["email"]
#             try:
#                 account = User.objects.exclude(pk = self.instance.pk).get(email = email)
#             except User.DoesNotExist:
#                 return email
#             raise forms.ValidationError('Email "%s" is already in use.' %account.email)

    
            
        
        
        
    
# import re
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(max_length=60)

#     class Meta:
#         model = User
#         fields = ("first_name", "last_name", "username", "email", "password1", "password2")


# class AccountUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ("first_name", "last_name", "email")

#     def clean_first_name(self):
#         if self.is_valid():
#             first_name = self.cleaned_data["first_name"]
#             if not re.match(r"^[A-Za-z]+$", first_name):
#                 raise forms.ValidationError("First name must contain only letters.")
#             return first_name

#     def clean_last_name(self):
#         if self.is_valid():
#             last_name = self.cleaned_data["last_name"]
#             if not re.match(r"^[A-Za-z]+$", last_name):
#                 raise forms.ValidationError("Last name must contain only letters.")
#             return last_name

#     def clean_email(self):
#         if self.is_valid():
#             email = self.cleaned_data["email"]
#             try:
#                 account = User.objects.exclude(pk=self.instance.pk).get(email=email)
#             except User.DoesNotExist:
#                 return email
#             raise forms.ValidationError(f'Email "{email}" is already in use.')


import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

    def clean_first_name(self):
        if self.is_valid():
            first_name = self.cleaned_data["first_name"]
            if not re.fullmatch(r"[A-Za-z]+", first_name):
                raise forms.ValidationError("First name must contain only alphabetic characters.")
            return first_name

    def clean_last_name(self):
        if self.is_valid():
            last_name = self.cleaned_data["last_name"]
            if not re.fullmatch(r"[A-Za-z]+", last_name):
                raise forms.ValidationError("Last name must contain only alphabetic characters.")
            return last_name

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            try:
                account = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError(f'Email "{email}" is already in use.')
