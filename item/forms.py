from django import forms

from .models import Items

# for avoide representation we make a class for disegning.
FORM_INPUT_CLASS = 'w-1/2 px-3 py-2 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model= Items
        fields = ('Name', 'category', 'description', 'image','price',)

        widgets ={
            'Name': forms.TextInput(attrs={'class':FORM_INPUT_CLASS}),
            'category': forms.Select(attrs={'class':FORM_INPUT_CLASS}),
            'description': forms.Textarea(attrs={'class':FORM_INPUT_CLASS}),
            'image': forms.FileInput(attrs={'class':FORM_INPUT_CLASS}),
            'price': forms.TextInput(attrs={'class':FORM_INPUT_CLASS}),
        }