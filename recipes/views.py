from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def root(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Biss Lee',
        'greetins': 'Good night'
    })


def about(request):
    title = 'Sobre'
    content = '''<ul>
            <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
            <li>Phasellus convallis nulla vitae tortor convallis, a pretium
            nisi fermentum.</li>
            <li>Donec vel ex pretium, lacinia dui a, consectetur dolor.</li>
            <li>Proin sit amet quam pulvinar, auctor velit ut,
            efficitur augue.</li>
            </ul>'''
    return page(title, content)


def contact(request):
    title = 'Contato'
    content = "<i>biss@biss.com.br</i>"
    return page(title, content)


def page(title, content):
    body = f'''
            <!DOCTYPE>
            <html>
                <head>
                    <title>Receitas :: {title}</title>
                </head>
                <body>
                    <h1>{title}</h1>
                    <hr>
                    <br>
                    <div>{content}</div>
                </body>
            </html>'''
    return HttpResponse(body)
