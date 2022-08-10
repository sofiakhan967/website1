
from multiprocessing import context
from django.shortcuts import render
from .models import Form,Post
import requests
from newsapi import NewsApiClient
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    details=Post.objects.all().order_by('-date_added')
    p=Paginator(details,3)
    page_number=request.GET.get('page')
    try:
        page_obj=p.get_page(page_number)
    except PageNotAnInteger:
        page_obj=p.page(1)
    except EmptyPage:
        page_obj=p.page(p.num_pages)        
    context={'page_obj': page_obj}
    return render(request,'home.html',context)

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        reason=request.POST['reason']
        form=Form(name=name,email=email,contact=contact,reason=reason)
        form.save()
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')   
    
def news(request):
    #API_KEY='4441a53713664f28a05b9b3ceddd5a52'
   # url=f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    #response=requests.get(url)
    #data=response.json()
    #articles=data['articles']
    # Initialise
    newsapi = NewsApiClient(api_key='4441a53713664f28a05b9b3ceddd5a52')

# /v2/everything
    all_articles = newsapi.get_everything(q='technology',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      
                                      language='en',
                                      
                                      page_size=50)
    #print(all_articles)
    article=all_articles['articles']
    p=Paginator(article,3)
    page_number=request.GET.get('page')
    try:
        page_obj=p.get_page(page_number)
    except PageNotAnInteger:
        page_obj=p.page(1)
    except EmptyPage:
        page_obj=p.page(p.num_pages)        
    context={'page_obj': page_obj}
    return render(request,'news.html',context)
      

def blog(request,slug):
    data=Post.objects.filter(slug=slug).first()
    context={'data':data}
    return render(request,'blog.html',context)    