from django import forms
from . models import Account,Address

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter Password',
    }))
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirm Password',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs )
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email address'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone number'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-lg'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
        

class UserAddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ["full_name", "house_name", "phone_number", "city", "district", "state", "country", "pin"]
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["full_name"].widget.attrs.update(
            {"class": "form-control mb-2 account-form" ,"placeholder":"Full Name"}
        )

        self.fields["house_name"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder":"House Name"}
        )

        self.fields["phone_number"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "pattern":"[0-9]{10}", "placeholder":"Phone Number"}
        )
       
        self.fields["city"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder":"City"}
        )

        self.fields["district"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder":"District"}
        )
        
        self.fields["state"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder":" State"}
        )

        self.fields["country"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder":"Country"}
        )

        self.fields["pin"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "pattern":"[0-9]{6}", "placeholder":"PIN code"}
        )
        