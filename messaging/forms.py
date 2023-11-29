from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'w-3/4 py-4 px-5 rounded-xl'
            }),
        }