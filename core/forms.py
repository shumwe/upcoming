from django import forms
from core.models import MailingList

class MailingSignUpForm(forms.ModelForm):
    class Meta:
        model = MailingList
        fields = ['subscriber_name', 'subscriber_email']
        