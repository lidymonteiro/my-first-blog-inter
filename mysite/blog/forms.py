from django import forms
from .models import PostPt, PostEn, PostEs

class PostFormPt(forms.ModelForm):

    class Meta:
        model = PostPt
        fields = ('title', 'text',)

class PostFormEn(forms.ModelForm):

    class Meta:
        model = PostEn
        fields = ('title', 'text',)

class PostFormEs(forms.ModelForm):

    class Meta:
        model = PostEs
        fields = ('title', 'text',)