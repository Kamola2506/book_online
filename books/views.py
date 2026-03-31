from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def home(request):
    return render(request, 'home.html')

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', id=book)
    else:
        form = BookForm(instance=book)
    return render(request, 'book_detail.html', {'form': form, 'book': book})

def book_update(request, pk):
    books = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('book')
    else:
            form = BookForm(instance=books)
    context = {
                'form': form
            }
    return render(request, 'book_update.html', context)

def book_delete(request, pk):
    books = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        books.delete()
        return redirect('book')
    return render(request, 'book_delete.html')