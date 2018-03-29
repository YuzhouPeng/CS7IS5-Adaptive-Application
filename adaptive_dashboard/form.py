from django import forms
class UserForm(forms.Form):
    username = forms.CharField(label="username", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="password", min_length=3, max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    gender = (
        ('male',"Male"),
        ('female',"Female"),
        ('other',"Other"),
    )
    username = forms.CharField(label="username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="password", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="confirmpassword", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="emailaddress", widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='gender', choices=gender)

# class Dashboard(forms.Form):
#     topics = forms.getlist('checks')