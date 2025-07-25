from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'maxlength': 500}),
        }
        labels = {
            'title': 'タイトル',
            'content': 'メモ内容',
            'tags': 'タグ',
        }
        
class TagSearchForm(forms.Form):
    search_tag = forms.CharField(
        label='タグ検索',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'タグ名を入力'})
    )