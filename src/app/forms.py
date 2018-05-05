from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from .models import Review, Booking, Contact_us, CheckAvailibility, Owner

User = get_user_model()

COMFORT= (
        ('low', 'Low'),
        ('sufficient', 'Sufficient'),
        ('good', 'Good'),
        ('excellent', 'Excellent'),
        ('super', 'Super'),
        ('i dont know', 'I dont know'),
    )

COST= (
        ('low', 'Low'),
        ('sufficient', 'Sufficient'),
        ('good', 'Good'),
        ('excellent', 'Excellent'),
        ('super', 'Super'),
        ('i dont know', 'I dont know'),
    )

QUALITY= (
        ('low', 'Low'),
        ('sufficient', 'Sufficient'),
        ('good', 'Good'),
        ('excellent', 'Excellent'),
        ('super', 'Super'),
        ('i dont know', 'I dont know'),
    )
EXTRA_FACILITIES = (
        ('wifi','Wifi'),
        ('loundry','Loundry'),
        ('food','Food'),
        ('maid','Maid')
    )

GENDER=(
        ('male','Male'),
        ('female','Female'),
    )
SHARING= [
    ('yes', 'Yes'), 
    ('no', 'No'),
]


class ReviewForm(forms.ModelForm):
    comfort = forms.CharField(widget=forms.Select(choices=COMFORT))
    cost = forms.CharField(widget=forms.Select(choices=COST))
    quality = forms.CharField(widget=forms.Select(choices=QUALITY))
    class Meta:
        model = Review
        fields = [
            'fname',
            'lname',
            'email',
            'pg_type',
            'comfort',
            'cost',
            'quality'
        ]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = [
            'fname',
            'lname',
            'email',
            'contact',
            'message'
        ]

class DateInput(forms.DateInput):
    input_type = 'date'


class AvailibilityForm(forms.ModelForm):
    available_from = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    # available_from = forms.DateField(widget=forms.SelectDateWidget)
    available_to = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = CheckAvailibility
        fields = [
            'name',
            'pg_type',
            'available_from',
            'available_to',
            'no_of_person',
            'area',
            'email'
        ]
        widgets = {
            'available_from': DateInput(),
        }


class BookingForm(forms.ModelForm):
    # facilities = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=EXTRA_FACILITIES,
    # )
    # arrival_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    arrival_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    departure_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect())
    sharing = forms.ChoiceField(choices=SHARING, widget=forms.RadioSelect())
    class Meta:
        model = Booking
        fields = [
            'fname',
            'lname',
            'pg_type',
            'no_of_person',
            'wifi',
            'loundry',
            'food',
            'maid',
            # 'facilities',
            'arrival_date',
            'departure_date',
            'gender',
            'sharing'
        ]

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    # def clean(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     email2 = self.cleaned_data.get('email2')
    #     if email != email2:
    #         raise forms.ValidationError("Emails must match")
    #     email_qs = User.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise forms.ValidationError("This email has already been registered")

    #     return super(UserRegisterForm,self).clean(*args, **kwargs)

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email

class OwnerForm(forms.ModelForm):
    sharing = forms.ChoiceField(choices=SHARING, widget=forms.RadioSelect())
    class Meta:
        model = Owner
        fields = [
            'name',
            'contact',
            'email',
            'pg_type',
            'description',
            'price',
            'sharing',
            'wifi',
            'loundry',
            'food',
            'maid',
            'image'
        ]