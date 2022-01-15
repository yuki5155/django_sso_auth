# Getting Started

## Build the Django Project

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
   
    return render(request, 'top/mypage.html')

```


## Run the redis container(recommended)

For saving cashe, usage of redis is recommended as more helpful features

The django default cache version may be upcomming 

Run those command on your command line

```

docker run -p 6379:6379 redis

```

## Run the MySQL container(recommended)

#### **`Dockerfile`**

```

FROM mysql

ENV MYSQL_ROOT_PASSWORD=sample
ENV MYSQL_DATABASE=sample
ENV MYSQL_USER=sample
ENV MYSQL_PASSWORD=sample

```

run those commands on your commandline

```

docker build -t mysql/test .
docker run mysql/test

```

# For Twitter

- create an account
- build a project 
- generate API KEY and Secret
- set the callback url

[DOC](./docs/twitter.md)