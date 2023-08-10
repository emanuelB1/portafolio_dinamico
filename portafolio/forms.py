from django import forms
from .models import ContactForm

class CustomContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Aplicar clases de Bootstrap a los campos del formulario
        self.fields['name'].widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'Nombre'})
        self.fields['email'].widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'Correo electrónico'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'Asunto'})
        self.fields['message'].widget.attrs.update({'class': 'form-control mb-3', 'rows': 3, 'placeholder': 'Mensaje'})
