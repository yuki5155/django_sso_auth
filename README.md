# Getting Started

## start Django Project

create those available pages with the render function

- http://localhost:8000
- http://localhost:8000/callback
- http://localhost:8000/mypage

example

```

def login_top(request):

    return render(request, 'top/index.html')

def callback(request):

    return render(request, 'top/callback.html')


def mypage(request):
   
    return(render(request, 'top/mypage.html'))

```

# For Twitter

- create an account
- build a project 
- generate API kEY and Secret
- set the callback url