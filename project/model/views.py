from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm

def news_list(request):
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})