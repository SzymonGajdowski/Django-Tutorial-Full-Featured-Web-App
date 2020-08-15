from django.shortcuts import render

posts = [
    {
        'title': 'Blog Post 1',
        'author': 'Jhon jhonny',
        'date_posted': '01-12-2019',
        'content': "Lorem ipsum dolor sit amet, consectetur adipiscing eit,"   
    },
    {
        'title': 'Blog Post 2',
        'author': 'Diego Esperanza',
        'date_posted': '14-03-2020',
        'content': "consectetur adipiscing elit"
    }
]

def home(request):
    content = {
        'posts': posts
    }
    return render(request, 'blog/home.html', content)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})


