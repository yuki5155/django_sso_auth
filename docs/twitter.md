## Before the Beginning

- create a twitter account
- build a project on the developer platform of twitter 
- generate API Key and Secret
- callback url

## Add These Variables on Setting.py

```

BASE_DOMAIN = "http://localhost:8000"
TW_CK = os.environ['tw_ck']
TW_CS = os.environ['tw_cs']
TW_AUTH_CALLBACK = '/callback'

```

## Example

#### **`view.py`**

```

from django.shortcuts import render
from libraries.my_auth import sso_auth_required, sso_login, sso_callback


def login_top(request):

    url = sso_login()

    return render(request, 'top/index.html', {'url': url})

@sso_callback
def callback(request):

    return render(request, 'top/callback.html')


@sso_auth_required
def mypage(request):
    
    # if authorized request.AUTH_STATE is true

    return(render(request, 'top/mypage.html'))

```

#### **`settings.py`**

```

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['NAME'],
            'USER': os.environ['USER'],
            'PASSWORD': os.environ['PASSWORD'],
            'HOST': os.environ['HOST'],
            'PORT': '3306',
            'OPTIONS': {
                'charset': 'utf8mb4',
                'sql_mode': 'TRADITIONAL,NO_AUTO_VALUE_ON_ZERO,ONLY_FULL_GROUP_BY',
            },
        },
    }

```