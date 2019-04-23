from django import forms

class NumberForm(forms.Form):
    #timezone = forms.ChoiceField(choices=['central','eastern','western'])
    your_num = forms.IntegerField(label='Your number: ')

class TimezoneForm(forms.Form):
    your_timezone = forms.ChoiceField(choices=[(1,"Central"),(2,"Eastern"),(3,"Western")])
