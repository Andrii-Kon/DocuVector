# converter/forms.py

from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    """
    A form for uploading new documents. The title field is optional
    and will default to the source PDF's filename if left blank.
    """
    class Meta:
        model = Document
        fields = ['title', 'source_pdf']

        # Use widgets to customize the appearance of form fields in HTML.
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Optional, defaults to filename'
            }),
        }

    def __init__(self, *args, **kwargs):
        """
        Override the default __init__ to mark the title field as not required.
        """
        super().__init__(*args, **kwargs)
        # This removes the `required` attribute from the HTML input tag.
        self.fields['title'].required = False