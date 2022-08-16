from django.shortcuts import render
from .models import Post

# posts = [
#     {
#         "author": 'Умар',
#         "title": 'Сегодня вечером',
#         "content": 'Я пойду в клуб',
#         "post_date": '16.08.2022'   
#     },
#     {
#         "author": 'Таисия',
#         "title": 'Мой секрет успеха',
#         "content": 'Я учусь каждый день',
#         "post_date": '16.08.2022'    
#     },
#     {
#         "author": 'Саадат',
#         "title": 'Жизнь с братом',
#         "content": 'Тяжелая жизнь',
#         "post_date": '16.08.2022'      
#     }
# ]
def home(request):
    context = {
        'posts': Post.objects.all()
        }
    return render(request, 'blog/home.html', context=context)

# def home(request):
#     return render(request, 'home.html', posts)