from django import forms
from ckeditor.fields import RichTextField, RichTextFormField

class Simple_Document(forms.Form):
    content = RichTextFormField()
    