from django.shortcuts import render
import pandas as pd


# Create your views here.
def landing(request):
    return render(request, 'single_pages/index.html')

def about_me(request):
    return render(request, 'single_pages/about_me.html')

def blog(request):
    df = pd.read_csv('./blog.csv')
    post_list = []
    for i, row in df.iterrows():
        post_list.append({
            "title": row["title"],
            "content": row["content"]
        })
    print(post_list)
    return render(request, 'single_pages/blog.html', context={'title': 'blog post', 'posts': post_list})

def career(request):
    return render(request, 'single_pages/career.html')

