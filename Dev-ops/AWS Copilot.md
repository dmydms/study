# AWS Copilot

## AWS Copliot이란?

AWS App Runner, Amazon EC2, AWS Fargate 에서의 빌드와 배포 및 실행을 쉽게 이용할 수 있게 해주는 open source CLI.  

## 사전 준비

- Route 53 domain name
- awscli 설치 및 인증
  - `brew awscli`
    - `~/.aws/config`, `~/.aws/credentials`가 생성되었는지 확인하기.
  - IAM > Access management > Users 메뉴의 Security credentials 탭에서 Access key ID 발급 및 Access Key ID와 Secrete Access Key 복사.
    - 주의, Secrete Access Key는 발급 직후 한번 밖에 조회 할 수 없음.
  - `aws configure` 실행 후 아래 네가지 항목에 대하여 응답.
    - cf. `-- profile [profile명]` 옵션을 사용하지 않으면 profile이 `default`로 저장됨.

    - ```bash
      AWS Access Key ID [None]: # IAM에서 발급 받은 Access Key ID
      AWS Secret Access Key [None]: # IAM에서 발급 받은 Secret Access Key
      Default region name [None]: # 서비스 리전. ex: ap-northeast-1
      Default output format [None]: # ex: json
      ```

  - 간단한 aws 명령어 입력해서 접속 확인
    - `aws s3 ls`

## Application 배포하기

이 문서는 [Deploy your first application](https://aws.github.io/copilot-cli/docs/getting-started/first-app-tutorial/) 문서를 참고함. 


- [본 문서](https://aws.github.io/copilot-cli/docs/developing/domain/)의 Attention  확인하기.  
- `copilot app init --domain mydomain.com`
- `copilot init` 실행 후, 아래 네가지 항목에 대해서 응답.
  1. "What would you like to name your application"
      - application 이름 설정.

  2. "Which service type best represents your service's architecture?"
      - Server 유형 선택.

      - ```bash
        Request-Driven Web Service (App Runner) # Serverless 
        Load Balanced Web Service (Internet to ECS on Fargate) # 최소 1대 서버 유지됨.
        ```

  3. "What do you want to name this service?"
      - 서비스 이름.  
      - cf. 하나의 application 내부에 여러 개의 서비스가 존재함.  

  4. "Which Dockerfile would you like to use for blah?"
      - docker file이 생성될 위치 혹은 이미 존재하는 docker image import.  
      - port 설정.
      - cf. 만약 custom path를 지정할 경우, 디렉토리가 자동으로 생성되지 않으니 미리 만들어두고 입력하기.  
      - ex. `./services/[service name]`  

  5. "Would you like to deploy a test environment?"
      - 테스트 배포 환경을 위한 설정.

- `copilot env init`
  1. What is your environment's name?
      - 환경 이름. 
      - ex. prod, test ...
  2. Which credentials would you like to use to create [env name]?
      - aws profile 선택

- `copilot svc deploy`
  - 배포.

- `copilot app delete`
  - application 삭제.  
  