from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import *
from account.models import User
from .forms import *


# prefetch_related('user_liked') Many to many feld uchun

def homeView(request):
    return render(request, "main/index.html",)

def BooksView(request):
    form = StockSearchForm(request.POST or None)
    queryset = Book.objects.select_related('genre', 'author').all()
    #Searching an item and category
    if request.method == 'POST':
        if form['genre'].value():
            queryset = queryset.filter(genre=form['genre'].value())
        if form['location'].value():
            queryset = queryset.select_related('genre', 'author').filter(location=form['location'].value())
        if form['query'].value():
            queryset = queryset.select_related('genre', 'author').filter(title__icontains=form['query'].value())    
                
    paginator = Paginator(queryset, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "form": form,
        "object_list": page_obj,
    }

    return render(request, "advert/book_list.html", context)


@login_required(login_url='/account/login/')
def MyBookView(request):
    author_book = Book.objects.select_related('genre', 'author').filter(author= request.user)
    return render(request, 'advert/my_advert.html', {"object": author_book})

def delete_view(request, url):
    obj = get_object_or_404(Book, slug = url)
    if obj.author != request.user:
        return HttpResponseServerError()
    else:
        context ={'object': obj}
        if request.method =="POST":
            obj.delete()
            return HttpResponseRedirect("/mybooks")
 
    return render(request, "advert/confirm.html", context)


class UpdateBook(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'advert/update_advert.html'
    fields = ("title", "author_pen", "genre", "description", "image")
    success_url = '/mybooks/'
    slug_field = 'slug'
    slug_url_kwarg = 'url'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            return HttpResponseServerError()
        return super(UpdateBook, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.select_related('author', 'genre').filter(author=self.request.user)
        context["books"] = book
        return context

    
def BookView(request, slug):
    book = Book.objects.select_related('genre', 'author').get(slug=slug)
    author_books = Book.objects.select_related('genre', 'author').exclude(slug = slug).filter(is_checked = True, author = book.author)[:16]
    related_books = Book.objects.select_related('genre', 'author').exclude(slug = slug).filter(is_checked = True, genre=book.genre)[:16]
    if book.is_checked == True or request.user.is_staff or book.author == request.user:
        context = {
            "object": book,
            "books": related_books,
            "author_books": author_books
        }
    return render(request, "advert/detail.html", context)

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'advert/create_advert.html'
    fields = ("title", "author_pen", "genre", "description", "image")
    success_url = '/mybooks/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.select_related('author', 'genre').filter(author=self.request.user)
        context["books"] = book
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.location = self.request.user.address
        form.instance.is_checked = False
        form.instance.is_ban = False
        return super().form_valid(form)
    
