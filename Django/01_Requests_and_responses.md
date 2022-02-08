# Requests and responses

## 예상 결과물

poll application

- 사람들이 득표수를 보고 투표할 수 있는 public site.
- 투표를 추가하고 변경하고 삭제하는 admin site.

## 프로젝트 생성하기

1. 코드를 저장할 폴더로 `cd`
2. `django-admin startproject mysite` 실행
    - 주의. built-in Python, Django 컴포넌트로 프로젝트의 이름을 짓는 것은 피해야함.
    - django (Django와 충돌)
        - test (built-in Python package와 충돌).
    - mysite 폴더 확인하기

        ```python
        # 디렉토리 구조
        mysite/
        manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py
        ```

        - `mysite/` 프로젝트 root 폴더로 이 폴더의 이름은 Django에 영향을 미치지 않기 때문에 원하는 이름으로 변경해도 괜찮음.
        - `manage.py/` Django project와 다양한 방법으로 interact 하는 command-line 도구. [django-admin and manage.py](https://docs.djangoproject.com/en/4.0/ref/django-admin/) 참고.
        - 내부 `mysite/`는 프로젝트의 Python package 임. 이 폴더의 이름은 Python package 이름으로 이 안에있는 무언가를 import 할 때 필요함. (e.g. mysite.urls)
        - `mysite/settings.py`: 장고 프로젝트에 대한 Settings/configuration. [Django settings](https://docs.djangoproject.com/en/4.0/topics/settings/) 참고
        - `mysite/urls.py`: Django 프로젝트를 위한 URL 선언.  Django-powered(?) site의 "table of contents". [URL dispatcher](https://docs.djangoproject.com/en/4.0/topics/http/urls/) 참고.
        - `mysite/asgi.py`: 프로젝트의 WSGI-compatible web servers를 위한 entry-point. [How to deploy with WSGI](https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/) 참고.

## 개발 서버

- root 폴더(outer `mysite/`)로 디렉토리 이동
- `python manage.py runserver` 실행
  - 주의. production 환경에서 이 서버를 사용하지 말 것.
  - <http://127.0.0.1:8000> 방문 및 "Congratulations!" 페이지 확인

cf.

- port 변경
  - `python manage.py runserver 8080`
- server's IP 변경.
  - `python manage.py runserver 0:8000`
  - 0 은 0.0.0.0의 shortcut
- Automatic reloading of runserver
  - 서버 코드가 바뀔 때마다 자동으로 reload 되기 때문에 서버 재시작이 불필요함.

## Polls app 생성하기

- `manage.py`가 있는 디렉토리로 이동.
- `python manage.py startapp polls` 실행
  - cf. Projects vs. apps
    - app: 어떤 일을 하는 web application으로 blog >system, database of public records 또는 a  small poll app이 있음.
    - project: 설정과 app들의 집합.
  
  - ```python
    polls/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py
    ```

## 첫번째 view 작성하기

- ```python
  # polls/views.py
  from django.http import HttpResponse

    def index(request):
        return HttpResponse("Hello, world. You're at the polls index.")
  ```

- 위 view를 호출하기 위해서는 URL을 연결해야하며, 연결을 위해서 URLconf가 필요함.
  `polls/urls.py` 생성
  - 생성 후 디렉토리 구조.

  - ```python
    polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
    ```
  
  - `polls/urls.py` 작성

     ```python
     from django.urls import path

     from . import views

     urlpatterns = [
        path('', views.index, name='index'),
     ]
     ```

  - `mysite/urls.py` 작성

    `polls.urls` 모듈에서 URLconf를 가리키기.

    ```python
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path('polls/', include('polls.urls')),
        path('admin/', admin.site.urls),
    ]
    ```

    - `include()`는 다른 URLconfs를 참조하는 것을 허용함.
    - Django는 `include()` 함수를 만날 때 마다, 해당 지점까지 일치하는 URL 부분을 잘라내고, 추가적인 처리를 위해서 URLconf에 나머지 문자열을 보냄.
    - `include()`함수는 다른 URL 패턴들을 포함할 때 꼭 사용해야함.  **admin.site.urls**의 경우만 예외.

    - `path()` 함수는 4개의 인자(argument)를 전달.
      - `route`: (required) URL 패턴을 담고있는 문자열.
      > route is a string that contains a URL pattern. When processing a request, Django starts at the first pattern in urlpatterns and makes its way down the list, comparing the requested URL against each pattern until it finds one that matches.
      >
      > Patterns don’t search GET and POST parameters, or the domain name. For example, in a request to <https://www.example.com/myapp/>, the URLconf will look for myapp/. In a request to <https://www.example.com/myapp/?page=3>, the URLconf will also look for myapp/.
      - `view`: (required) Django가 일치하는 패턴을 찾으면, HTTPRequest 객체와 함께 특정 view function 을 호출함.
      >When Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first argument and any “captured” values from the route as keyword arguments. We’ll give an example of this in a bit.

      - `kwargs`: 이 튜토리얼에서 사용하지 않음.
      - `name`: URL 이름을 지정하면 Django 다른 곳, 특히 템플릿 내에서 명확히 참조 가능. 이 기능을 사용하면 하나의 파일만 수정하면 URL pattern을 global changes 하는 것이 가능.

  - `python manamge.py runserver`
    - <http://localhost:8000/polls/> 접속 후, “Hello, world. You’re at the polls index.” 확인하기.

**참고**
인용구는 해석이 정확하지 않아 첨부함.
