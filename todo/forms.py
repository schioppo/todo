from django import forms
from .models import Todo


class CustomCreateForm(forms.ModelForm):
    class Meta():
        model = Todo
        fields = ('title', 'description', 'author')
        widgets = {
            'title': forms.TextInput(attrs={'style': "width: 100%; padding: 12px 20px; margin: 8px 0; display: border: 1px solid black; border-radius: 4px;"}),
            'description': forms.Textarea(attrs={'style': "width: 100%; padding: 12px 20px; margin: 8px 0; border: 1px solid black; border-radius: 4px;"}),
            'author': forms.Select(attrs={'style': "width: 100%; padding: 12px 20px; margin: 8px 0; border: 1px solid black; border-radius: 4px;"}),
        }


class CustomUpdateForm(forms.ModelForm):
    class Meta():
        model = Todo
        fields = ('title', 'description', 'done')
        widgets = {
            'title': forms.TextInput(attrs={'style': "width: 100%; padding: 12px 20px; margin: 8px 0; display: border: 1px solid black; border-radius: 4px;"}),
            'description': forms.Textarea(attrs={'style': "width: 100%; padding: 12px 20px; margin: 8px 0; border: 1px solid black; border-radius: 4px;"}),
        }
