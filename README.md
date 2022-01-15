# Getting Started

## Build the Django Project

create those available pages with the render function

- http://localhost:8000
- http://localhost:8000/callback
- http://localhost:8000/mypage

example

## Run the redis container(recommended)

For saving cashe, redis is recommended to use

django default cache version is upcomming






```

def login_top(request):

    return render(request, 'top/index.html')

def callback(request):

    return render(request, 'top/callback.html')


def mypage(request):
   
    return render(request, 'top/mypage.html')

```

# For Twitter

- create an account
- build a project 
- generate API kEY and Secret
- set the callback url