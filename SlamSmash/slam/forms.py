from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import TextInput,PasswordInput,EmailInput

from .models import SlamBook

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Username',
            'class':'form-control'
        })
    )
    password = forms.CharField(
        max_length=250,
        widget=PasswordInput(attrs={
            'placeholder':'Password',
            'class':'form-control'
        })
    )
    class Meta:
        model = User
        fields = ('username','password')

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Username',
            'class':'form-control'
        })
    )
    first_name = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'First Name',
            'class':'form-control'
        })
    )
    last_name = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Last Name',
            'class':'form-control'
        })
    )
    email = forms.EmailField(
        max_length=250,
        widget=EmailInput(attrs={
            'placeholder':'Email',
            'class':'form-control'
        })
    )
    password1 = forms.CharField(   
        max_length=250,
        widget=PasswordInput(attrs={
            'placeholder':'Password',
            'class':'form-control'
        })
    )
    password2 = forms.CharField(   
        max_length=250,
        widget=PasswordInput(attrs={
            'placeholder':'Confirm Password',
            'class':'form-control'
        })
    )

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    
    def save(self,commit=True):
        user = super(SignUpForm,self).save(commit=False)
        #user.username = cleaned_data['username']
        #user.first_name = cleaned_data['first_name']
        #user.last_name = cleaned_data['last_name']
        #user.email = cleaned_data['email']

        if commit:
            user.save()
        
        return user

class SlamForm(forms.ModelForm):
    my_name = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Name',
            'class':'form-control'
        })
    )
    my_nickname = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Nickname according to me',
            'class':'form-control'
        })
    )
    my_address = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Adress',
            'class':'form-control'
        })
    )
    my_mobile_number = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Mobile Number',
            'class':'form-control'
        })
    )
    my_email = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Email Id',
            'class':'form-control'
        })
    )
    my_birth_day = forms.CharField(
        widget=TextInput(attrs={
            'placeholder':'Birth Day Date',
            'class':'form-control'
        })
    )
    my_zodiac_sign = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Zodiac Sign',
            'class':'form-control'
        })
    )
    my_crushes = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Crush Names',
            'class':'form-control'
        })
    )
    my_happiest_moment = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Happiest moments with me',
            'class':'form-control'
        })
    )
    my_favourite_dishes = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Favourite Dishes',
            'class':'form-control'
        })
    )
    my_favourite_sports = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Favourite Sports',
            'class':'form-control'
        })
    )
    my_favourite_places = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your favourite Places',
            'class':'form-control'
        })
    )
    my_favourite_actor = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Favourite Actor',
            'class':'form-control'
        })
    )
    my_favourite_actress = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Favourite Actress',
            'class':'form-control'
        })
    )
    my_favourite_webiste = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Favourite Website',
            'class':'form-control'
        })
    )
    my_favourite_festival = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Favourite Festival',
            'class':'form-control'
        })
    )
    my_favourite_song = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Favourite Song',
            'class':'form-control'
        })
    )
    my_ideal = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Role Model',
            'class':'form-control'
        })
    )
    opinion_about_you = forms.CharField(
        max_length=250,
        widget=TextInput(attrs={
            'placeholder':'Your Opinion about me',
            'class':'form-control'
        })
    )
    class Meta:
        model = SlamBook
        fields = (
            'my_name',
            'my_nickname',
            'my_address',
            'my_mobile_number',
            'my_email',
            'my_birth_day',
            'my_zodiac_sign',
            'my_crushes',
            'my_happiest_moment',
            'my_favourite_dishes',
            'my_favourite_sports',
            'my_favourite_places',
            'my_favourite_actor',
            'my_favourite_actress',
            'my_favourite_webiste',
            'my_favourite_festival',
            'my_favourite_song',
            'my_ideal',
            'opinion_about_you',
        )
    #def __init__(self, *args, **kwargs):
        #user = kwargs.pop('user','')
        #super(DocumentForm, self).__init__(*args, **kwargs)
        #self.fields['user_defined_code']=forms.ModelChoiceField(queryset=UserDefinedCode.objects.filter(owner=user)