from django import forms

class LogForm(forms.Form):
	player = forms.IntegerField()
	file = forms.FileField()
