from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

def tag_search(request):
    tag = request.GET.get('tag')
    notes = Note.objects.filter(tags__name__in=[tag]) if tag else Note.objects.none()
    return render(request, 'notes/tag_search.html', {'notes': notes, 'tag': tag})

def note_form(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')  # 保存後にリスト画面などへ
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})