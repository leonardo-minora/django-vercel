from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <head>
          <title>Vercel - django</title>
        </head>
        <body>
            <h1>Vercel - Exemplo de app web em django!</h1>
            <p>A hora atual { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)