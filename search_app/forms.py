from django import forms
from django.core.validators import RegexValidator

search_string_validator = RegexValidator(r'^[a-zA-Z]{3,}$', "No special characters and numbers are allowed in search strings")

#Class to take the string from the post request after user submitting a request in home page
class SearchStringForm(forms.Form):
    search_string = forms.CharField(
        label='search_string',
        max_length=100,
        validators=[search_string_validator]
    )
