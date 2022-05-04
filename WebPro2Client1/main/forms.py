from .models import Module1, Document
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django import forms


class DocumentForm(forms.ModelForm):
    description = forms.CharField(max_length=50)
    document = forms.FileField()

    class Meta:
        model = Document
        fields = ('description', 'document')


class NewsForm(ModelForm):

    class Meta:
        model = Module1
        fields = ['title', 'news']

        widgets ={
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Жаңалық атауы'
        }),
            "news": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Жаңалықты енгізу'
            })
      }


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=True)
    subject = forms.CharField(label='About', required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)
