# [How to install Django](https://docs.djangoproject.com/en/4.0/topics/install/#how-to-install-django)

1. Install Apache and mod_wsgi.
    - production에 배포할 준비가 될 때 까지 설치하지 않아도 됨.

2. Get your database running.
    - 당분간 [SQLite](https://www.sqlite.org/index.html) 사용하기.]
    - PostgreSQL 설치하기 ([참고 문서](https://www.sqlshack.com/setting-up-a-postgresql-database-on-mac/))
      - `brew install postgresql`
      (`postgres -V` 로 설치 확인.)
      - `psql postgres` (postgresql 접속)
      - Postgres DB Server 설정.

        ```sql
        # 유저 생성 
        CREATE ROLE newUser WITH LOGIN PASSWORD ‘password’;

        # role 변경 
        ALTER ROLE newUser CREATEDB;

        # DB 종료
        \q

        # 새로 생성한 유저로 접속 
        psql postgres -U newuser
        
        # DB 생성하기
        CREATE DATABASE database_name 

        # DB 리스트 확인하기 
        \ l

        # port 정보 확인하기 (Django `settings.py`에 넣을 때 확인하기 위해서.)
        \conninfo
        ```

3. Django 설치

    a. [pip](https://pip.pypa.io/en/stable/) 설치.
  
    - 쉬운 설치 방법은 [standalone pip install](https://pip.pypa.io/en/latest/installation/) 참고.
    - 이미 pip이 설치되어 있다면, 최신 상태 유지하기. (오래된 버전이면 설치가 동작하지 않을 수 있음.)

    b. [venv](https://docs.python.org/3/tutorial/venv.html) 살펴보기.

    - 이 도구는 독립된 Python 환경을 제공함.
    - 관리자 권한 없이 패키지들을 설치할 수 있음.
    - 가상환경 생성 방법은 [contributing tutorial](https://docs.djangoproject.com/en/4.0/intro/contributing/) 참고.
        - 가상환경 생성 방법 요약  

        ```bash
        # 가상환경 생성
        $ python3 -m venv ~/.virtualenvs/djangodev

        # 가상환경 실행
        $ source ~/.virtualenvs/djangodev/bin/activate
        
        # source가 동작을 안 할 경우 
        $ . ~/.virtualenvs/djangodev/bin/activate

        # 가상환경 종료
        deactivate
        ```

    c. 가상환경 생성 및 실행 후 아래 명령어 입력.
        `python -m pip install Django`

4. distribution-specific package 설치
    - 잘 모르겠음. [distribution specific notes](https://docs.djangoproject.com/en/4.0/misc/distributions/)를 참고.

5. development version 설치
    - 생략

cf. 설치 확인하기.

- python 실행.

- ```python
    >>> import django
    >>> print(django.get_version())
    ```
