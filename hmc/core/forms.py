from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "date_of_event": forms.DateInput(attrs={"type": "date"}),
            "phone_number": forms.NumberInput(attrs={"type": "number"})
        }