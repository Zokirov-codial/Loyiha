from django import forms
from .models import *

class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = ['ism', 'jins', 't_sana', 'kitob_soni', 'tirik']

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['talaba', 'kitob', 'kutubxonachi', 'qaytarish_sana', 'qaytardi']


class KutubxonachiForm(forms.ModelForm):
    class Meta:
        model = Kutubxonachi
        fields = ['ism', 'ish_vaqti']



class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = ['nom', 'yonalish', 'asosiy', ]


class UstozForm(forms.ModelForm):
    class Meta:
        model = Ustoz
        fields = ['ism', 'jins', 'yosh', 'daraja', 'fan', ]
