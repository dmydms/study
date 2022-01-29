# MySQL 설치하기

1. `brew services list`
    - 이미 동작하는 mysql이 있는지 확인하기. 
    - [Homebrew Services](https://github.com/Homebrew/homebrew-services)
        - Manage background services with macOS' launchctl daemon manager.
    - mysql 다른 버전이 동작하고 있으면 정지시키기.
        - `brew services stop mysql`
2. `brew update`
    - [ ] TODO: 꼭 해야하는가? 왜 하는가? 
    - [Homebrew official docs](https://docs.brew.sh/FAQ)
    - Update local packages. First update all package definitions (formulae) and Homebrew itself.
3. `brew install mysql`
    - MySQL 설치
4. `mysql --version`
    - MySQL이 잘 설치되었는지 확인.
5. `brew services start mysql`
    - MySQL 서버 시작.
    - MySQL 서버 종료.
        - `brew services stop mysql`
        - `mysql.server stop`
6. `mysql_secure_installation`
    - 보안 설정.
        - You can set a password for root accounts.
        - You can remove root accounts that are accessible from outside the local host.
        - You can remove anonymous-user accounts.
        - You can remove the test database (which by default can be accessed by all users, even anonymous users), and privileges that permit anyone to access databases with names that start with test_.
7. `mysql -uroot -p`
    - `-uroot`
        - `-u root`의 shorthand
        - User for login if not current user.
    - `-p` 
        - Password to use when connecting to server. If password is
                      not given it's asked from the tty.


> cf. https://dalya-tech.tistory.com/37