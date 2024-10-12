from django.http import HttpResponse

# Home page view
def home_view(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>Hello, Selva Balaji!</h1>
        <p>Welcome to my Django app.</p>
        <form action="/about/">
            <button type="submit">About Me</button>
        </form>
    </body>
    </html>
    """
    return HttpResponse(html)

# About page view
def about_view(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }
        </style>
    </head>
    <body>
        <h1>About Me</h1>
        <p>Full Name : Selva Balaji</p>
        <p>Roll No : 22uit030</p>
        <p>Dept : B.Tech IT</p>
        <p>Class : III year IT-A</p>
    </body>
    </html>
    """
    return HttpResponse(html)

