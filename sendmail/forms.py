# coding=utf-8
# sendemail/forms.py
from django import forms


class ContactForm(forms.Form):
    to_email_list = forms.FileField()
    subject = forms.CharField(required=True)
    file1 = forms.FileField()
