from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Note,Tag
from .forms import NoteForm,TagSearchForm

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

def tag_search(request, tag):
    tag_obj = get_object_or_404(Tag, name=tag)
    notes = Note.objects.filter(tags=tag_obj).order_by('-created_at')
    return render(request, 'notes/tag_search.html', {
        'tag': tag_obj,
        'notes': notes
    })

def note_form(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            try:
                note = form.save(commit=False)
                note.save()
                
                # タグの処理
                tags_str = request.POST.get('tags', '')
                if tags_str:
                    tag_names = [t.strip() for t in tags_str.split(',')]
                    for tag_name in tag_names:
                        if tag_name:
                            tag, created = Tag.objects.get_or_create(name=tag_name)
                            note.tags.add(tag)
                
                messages.success(request, 'メモが保存されました。')
                return redirect('note_list')
            except Exception as e:
                messages.error(request, f'保存中にエラーが発生しました: {str(e)}')
        else:
            messages.error(request, 'フォームの入力内容に問題があります。')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

def search_by_tag(request):
    form = TagSearchForm(request.GET)
    notes = None
    search_tag = None
    
    # GETパラメータからタグ名を取得
    tag_name = request.GET.get('tag')
    if tag_name:
        # タグ名が指定されている場合は、そのタグを持つメモを検索
        tag = get_object_or_404(Tag, name=tag_name)
        notes = Note.objects.filter(tags=tag).distinct()
        search_tag = tag_name
    elif form.is_valid():
        # フォームから検索する場合
        search_tag = form.cleaned_data.get('search_tag')
        if search_tag:
            notes = Note.objects.filter(tags__name__icontains=search_tag).distinct()
    
    return render(request, 'notes/tag_search.html', {
        'form': form,
        'notes': notes,
        'search_tag': search_tag
    })