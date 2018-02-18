from django.shortcuts import render
from django.http import HttpResponse
from .models import MyArticle
def index(request):
    articles = MyArticle.object.all()
    return render(request, 'firstapp/list.html', {'articles':articles})

# Create your views here.
def get_article(request, article_id):
    return  render(request, 'firstapp/list.html')


'''article = [
   {
       'id': 1,
       'title': 'First news',
       'text': 'This is the worst first article'
   },
   {
       'id': 2,
       'title': 'Second news',
       'text': 'This is the amazing second article'
   }]'''
