from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Demoapp.models import Video,AdminLogin,Movie,Review,Check

class Imageform(forms.ModelForm):
    class Meta:
        model = Video
        fields = "__all__"

class Adminform(forms.ModelForm):
    class Meta:
        model = AdminLogin
        fields = "__all__"
        permisions = (
            ('can_change_post_slug')
        )

class CreationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class Movieform(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"  


class Reviewform(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"  

class ImageCh(forms.ModelForm):
    class Meta:
        model = Check
        fields = "__all__"




