# MySQL 설치하기

1. `brew services list`
    - 이미 동작하는 mysql이 있는지 확인하기. 
    - [Homebrew Services](https://github.com/Homebrew/homebrew-services)
        - Manage background services with macOS' launchctl daemon manager.
    - mysql 다른 버전이 동작하고 있으면 정지시키기.
        - `brew services stop mysql`
2. `brew update`
    - [ ] TODO(question): 이 과정에서 꼭 해야하는가?
    - [How do I update my local packages?](https://docs.brew.sh/FAQ#how-do-i-update-my-local-packages)
    - Update local packages. First update all package definitions (formulae) and Homebrew itself.
3. `brew install mysql`
    - MySQL 설치
4. `mysql --version`
    - MySQL이 잘 설치되었는지 확인.
5. `brew services start mysql`
    - MySQL 서버 시작.
    - cf. MySQL 서버 종료.
        - `brew services stop mysql`
        - `mysql.server stop`
6. `mysql_secure_installation`
    - [보안 설정.](https://dev.mysql.com/doc/refman/8.0/en/mysql-secure-installation.html)
        - You can set a password for root accounts.
        - You can remove root accounts that are accessible from outside the local host.
        - You can remove anonymous-user accounts.
        - You can remove the test database (which by default can be accessed by all users, even anonymous users), and privileges that permit anyone to access databases with names that start with test_.
7. `mysql -uroot -p`
    - `-uroot`
        - `-u root`의 shorthand
        - User for login if not current user.
    - `-p` 
        - Password to use whㅌen connecting to server. If password is
                      not given it's asked from the tty.

8. ``` SQL
    # mysql 데이터베이스 선택.
    USE mysql;

    # 유저 추가 및 비밀번호 지정.
    CREATE USER 'name'@'localhost' IDENTIFIED BY 'blah';

    # name 유저에게 '모든 권한'을 부여.
    GRANT ALL PRIVILEGES ON *.* TO 'name'@'%' WITH GRANT OPTION;
        #
        # 이 단계에서 아래 에러 발생. 
        # ERROR 1410 (42000): You are not allowed to create a user with GRANT
        #
        # 🤔 문제 원인:
        # 호스트가 'localhost'인 USER를 생성했으나, '%'에는 'localhost'가 포함되지 않기 때문에
        # 서로 다른 USER라고 인식되어 권한 부여에 실패함. 
        #
        # 💡 해결 방법:
        # 호스트가 '%'인 USER를 새로 생성.
        # 
        # 📝 참고 문서:
        # https://stackoverflow.com/questions/10823854/using-for-host-when-creating-a-mysql-user

    # 권한 지정 flush.
    FLUSH PRIVILEGES;

    # DB 추가.
    CREATE DATABASE pabp;
    ```
<br/>

----- 

### 참고 문서
cf. MinsangK(twt. [@minsangk](https://twitter.com/minsangk))님 - Backend Pracktice / Tutorial 1. 환경 설정  
cf. https://dev.mysql.com/doc/  
cf. https://dalya-tech.tistory.com/37