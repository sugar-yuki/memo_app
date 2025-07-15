from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'maxlength': 500}),
        }
        labels = {
            'title': 'タイトル',
            'content': 'メモ内容',
            'tags': 'タグ',
        }