# GitHub Actions 소개

GitHub Actions는 GitHub에서 코드 자동화 및 CI/CD 작업을 처리할 수 있는 도구다. 소프트웨어 개발 워크플로우를 자동화하여 통합과 배포 과정을 간소화하고 효율성을 높인다.

## GitHub Actions의 주요 기능

- **자동화된 워크플로우**: 소프트웨어 개발 및 배포 프로세스를 자동화하여 반복 작업을 줄이고 개발 속도를 향상시킨다.
- **다양한 이벤트에 대한 반응**: GitHub 저장소에서 발생하는 다양한 이벤트(예: 푸시, 풀 리퀘스트, 이슈 생성 등)에 따라 작업을 트리거할 수 있다.
- **언어와 플랫폼에 구애받지 않음**: 다양한 운영 체제에서 여러 프로그래밍 언어와 도구를 지원하여 다양한 프로젝트에 유연하게 적용할 수 있다.
- **재사용 가능한 컴포넌트**: GitHub 커뮤니티에서 제공하는 다양한 Actions를 재사용하여 워크플로우를 빠르고 쉽게 구성할 수 있다.
- **병렬 및 매트릭스 빌드**: 여러 작업을 병렬로 실행하거나 매트릭스 전략을 사용하여 다양한 환경에서 테스트를 수행할 수 있다.
- **비밀 관리 및 보안**: 환경 변수와 시크릿을 안전하게 관리하여 민감한 정보를 보호할 수 있다.

## GitHub Actions 구성 요소

1. **워크플로우(Workflows)**
    - 워크플로우는 하나 이상의 작업(Job)을 포함하며, `.github/workflows` 디렉토리에 YAML 파일로 저장된다.
    - 특정 이벤트에 의해 자동으로 실행되며, 프로젝트의 자동화된 프로세스를 정의한다.
2. **이벤트(Events)**
    - 워크플로우는 저장소에서 발생하는 특정 이벤트에 의해 트리거된다.
    - 예를 들어, `push`, `pull_request`, `issue`, `schedule` 등의 이벤트가 있다.
    - 이벤트는 워크플로우의 시작점을 정의하며, 필요한 조건에 따라 워크플로우가 실행된다.
3. **작업(Jobs)**
    - 작업은 워크플로우 내에서 실행되는 일련의 단계(Steps)로 구성된다.
    - 각 작업은 독립적으로 실행되거나 다른 작업과 의존성을 가질 수 있다.
    - 동일한 러너에서 또는 다른 러너에서 병렬로 실행될 수 있다.
4. **단계(Steps)**
    - 각 작업은 하나 이상의 단계로 구성된다.
    - 단계는 개별 명령을 실행하거나, 다른 액션을 호출하여 특정 작업을 수행한다.
    - 단계는 순차적으로 실행되며, 이전 단계의 결과를 사용할 수 있다.
5. **액션(Actions)**
    - 액션은 워크플로우에서 재사용할 수 있는 독립적인 명령 모듈이다.
    - 자체 액션을 작성할 수 있으며, GitHub Marketplace에서 다양한 커뮤니티 액션을 찾아 사용할 수 있다.
    - 액션은 JavaScript, Docker 컨테이너 등 다양한 방식으로 구현될 수 있다.
6. **러너(Runners)**
    - 러너는 GitHub Actions 워크플로우가 실행되는 서버다.
    - GitHub은 호스팅된 러너를 제공하며, 사용자는 자체 호스팅 러너를 설정할 수도 있다.
    - 호스팅된 러너는 다양한 운영 체제(예: Ubuntu, Windows, macOS)를 지원한다.

## GitHub Actions 사용 예시

### 간단한 CI 파이프라인 설정

```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: 설정된 Node.js 버전 사용
      uses: actions/setup-node@v3
      with:
        node-version: '16'

    - name: 종속성 설치
      run: npm install

    - name: 테스트 실행
      run: npm test
```

### 배포 파이프라인 설정

```yaml
name: Deploy

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: 빌드
      run: npm run build

    - name: 배포
      uses: easingthemes/ssh-deploy@v2
      with:
        ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}
        remote-user: user
        server-ip: 192.168.1.1
        remote-path: /var/www/app
```

## GitHub Actions의 고급 기능

1. **캐시(Caching)**
    - CI 작업에서 자주 발생하는 종속성 설치를 캐싱하여 빌드 속도를 크게 개선할 수 있다.
    - 예를 들어, Node.js 프로젝트에서는 `npm ci` 명령으로 종속성을 설치할 때, 종속성 캐시를 사용하여 불필요한 네트워크 요청을 줄일 수 있다.
    
    ```yaml
    - name: 종속성 캐시
      uses: actions/cache@v3
      with:
        path: ~/.npm
        key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
        restore-keys: |
          ${{ runner.os }}-node
    ```
    
2. **매트릭스 전략(Matrix Strategy)**
    - 동일한 테스트 작업을 여러 환경에서 실행하기 위해 매트릭스 전략을 사용할 수 있다.
    - 이를 통해 다양한 Node.js 버전에서 애플리케이션의 호환성을 테스트할 수 있다.
    
    ```yaml
    jobs:
      build:
        runs-on: ubuntu-latest
        strategy:
          matrix:
            node-version: [12.x, 14.x, 16.x]
    
        steps:
        - uses: actions/setup-node@v3
          with:
            node-version: ${{ matrix.node-version }}
        - run: npm install
        - run: npm test
    ```
    
3. **컨디셔널 실행(Conditional Execution)**
    - 특정 조건이 충족될 때만 단계 또는 작업을 실행하도록 할 수 있다.
    - 예를 들어, 특정 파일이 변경된 경우에만 배포 작업을 실행하거나, 특정 브랜치에 푸시된 경우에만 작업을 수행하도록 설정할 수 있다.
    
    ```yaml
    steps:
    - name: 배포
      run: ./deploy.sh
      if: github.ref == 'refs/heads/main'
    ```
    
4. **병렬 처리**
    - GitHub Actions는 여러 작업을 병렬로 실행할 수 있어, 테스트 시간을 단축할 수 있다.
    - 예를 들어, 프론트엔드와 백엔드 작업을 동시에 실행하도록 설정할 수 있다.
    
    ```yaml
    jobs:
      frontend:
        runs-on: ubuntu-latest
        steps:
        - run: npm run test:frontend
    
      backend:
        runs-on: ubuntu-latest
        steps:
        - run: npm run test:backend
    ```
    

## GitHub Actions 추가 예시

### 멀티 OS에서 테스트 실행

다양한 운영 체제에서 애플리케이션을 테스트하여 호환성을 확인한다.

```yaml
name: CI on Multiple OS

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ ubuntu-latest, windows-latest, macos-latest ]
        node-version: [ 14, 16, 18 ]

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: Node.js 설정
      uses: actions/setup-node@v3
      with:
        node-version: ${{ matrix.node-version }}

    - name: 종속성 설치
      run: npm install

    - name: 테스트 실행
      run: npm test
```

- 여러 운영 체제(Ubuntu, Windows, macOS)에서 테스트를 병렬로 실행.
- Node.js의 다양한 버전에서 애플리케이션의 호환성 테스트 수행.

### Docker 이미지 빌드 및 푸시

Docker 이미지를 빌드하고 Docker Hub에 푸시하여 배포를 자동화한다.

```yaml
name: Docker Build and Push

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: Docker 로그인
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}

    - name: Docker 이미지 빌드
      run: docker build -t myapp:${{ github.sha }} .

    - name: Docker 이미지 푸시
      run: docker push myapp:${{ github.sha }
```

- Docker Hub에 로그인하여 이미지를 푸시.
- 커밋 해시를 태그로 사용하여 고유한 이미지 생성.
- 빌드한 Docker 이미지를 Docker Hub에 업로드.

### AWS에 애플리케이션 배포

AWS Elastic Beanstalk에 애플리케이션을 배포한다.

```yaml
name: Deploy to AWS

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: AWS 설정
      uses: aws-actions/configure-aws-credentials@v2
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-east-1

    - name: 애플리케이션 압축
      run: zip -r myapp.zip .

    - name: 애플리케이션 버전 생성
      run: |
        aws elasticbeanstalk create-application-version --application-name my-app --version-label ${{ github.sha }} --source-bundle S3Bucket=my-bucket,S3Key=myapp.zip

    - name: Elastic Beanstalk 환경 업데이트
      run: |
        aws elasticbeanstalk update-environment --environment-name my-env --version-label ${{ github.sha }}
```

- AWS 자격 증명을 설정하여 AWS 서비스에 접근.
- 애플리케이션을 압축하여 S3에 업로드.
- Elastic Beanstalk 환경을 업데이트하여 새로운 버전 배포.

### 코드 린트 및 포맷 검사

코드의 품질을 유지하기 위해 린트와 포맷 검사를 자동화한다.

```yaml
name: Lint and Format

on:
  pull_request:
    branches: [ main ]

jobs:
  lint:
    runs-on: ubuntu-latest

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: Node.js 설정
      uses: actions/setup-node@v3
      with:
        node-version: '16'

    - name: 종속성 설치
      run: npm install

    - name: ESLint 실행
      run: npm run lint

    - name: Prettier 실행
      run: npm run format:check
```

- ESLint를 사용하여 코드의 문법 및 스타일 검사.
- Prettier를 사용하여 코드 포맷 검사.
- Pull Request 생성 시 자동으로 린트와 포맷 검사 실행.

### 패키지 퍼블리싱

npm 패키지를 자동으로 배포한다.

```yaml
name: Publish Package

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  publish:
    runs-on: ubuntu-latest

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: Node.js 설정
      uses: actions/setup-node@v3
      with:
        node-version: '16'
        registry-url: 'https://registry.npmjs.org/'

    - name: npm 로그인
      run: echo "//registry.npmjs.org/:_authToken=${{ secrets.NPM_TOKEN }}" > ~/.npmrc

    - name: 패키지 빌드
      run: npm run build

    - name: 패키지 퍼블리싱
      run: npm publish
```

- 태그가 `v*.*.*` 형식으로 푸시될 때 패키지 빌드 및 퍼블리싱 수행.
- npm 레지스트리에 로그인하여 패키지 업로드.
- 퍼블리싱 전에 패키지 빌드 실행.

### Slack 알림 통합

빌드 상태를 Slack 채널에 알림으로 전송한다.

```yaml
name: CI with Slack Notification

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: Node.js 설정
      uses: actions/setup-node@v3
      with:
        node-version: '16'

    - name: 종속성 설치
      run: npm install

    - name: 테스트 실행
      run: npm test

    - name: Slack 알림
      if: always()
      uses: slackapi/slack-github-action@v1.23.0
      with:
        payload: |
          {
            "text": "빌드 상태: ${{ job.status }}"
          }
      env:
        SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
```

- 빌드 작업이 완료되면 Slack에 빌드 상태를 알림.
- `if: always()`를 사용하여 성공 또는 실패 여부에 관계없이 알림 전송.
- Slack Bot Token을 사용하여 인증.

## GitHub Actions의 한계와 해결 방안

1. **러너의 자원 제한**
    - GitHub 호스팅 러너는 CPU, 메모리 등의 자원 제한이 있다. 이를 해결하기 위해 자체 호스팅 러너를 설정하여 자원을 확장할 수 있다.
    - 또한, 워크플로우를 최적화하여 빌드 시간을 줄이는 것도 중요한 전략이다.
2. **로그 관리의 복잡성**
    - 워크플로우가 복잡해질수록 로그를 추적하고 디버깅하는 데 어려움이 발생할 수 있다. 이를 해결하기 위해 로그를 잘 관리하고, 오류 발생 시 Slack과 같은 툴과 통합하여 실시간 알림을 받을 수 있다.
3. **비용 관리**
    - 무료 제공 범위를 넘어서면 GitHub Actions의 사용 비용이 발생할 수 있다. 이를 방지하기 위해 워크플로우 실행을 최적화하거나, 자체 호스팅 러너를 이용하여 비용을 절감할 수 있다.

## 결론: GitHub Actions를 사용하는 이유

GitHub Actions는 개발 팀이 소프트웨어 개발 과정을 자동화하고, 보다 효율적으로 배포할 수 있게 도와준다. 이 도구를 사용하면 복잡한 스크립트나 외부 서비스 없이도 GitHub 내에서 직접적인 자동화와 통합이 가능하다. 다음과 같은 이점을 제공한다:

- **통합된 환경**: 코드 저장소와 자동화 도구가 동일한 플랫폼 내에 있어 설정과 관리가 용이하다.
- **확장성**: 다양한 액션과 커스텀 워크플로우를 통해 프로젝트 요구에 맞게 유연하게 확장할 수 있다.
- **커뮤니티 지원**: GitHub Marketplace에 다양한 커뮤니티 액션이 있어 문제 해결과 워크플로우 개선에 도움을 받을 수 있다.
- **비용 효율성**: 기본 제공되는 호스팅 러너를 활용하거나 필요에 따라 자체 러너를 설정하여 비용을 절감할 수 있다.
- **보안 강화**: 시크릿 관리와 권한 설정을 통해 안전한 자동화를 구현할 수 있다.

## 추가 GitHub Actions 예시

### 멀티 OS에서 테스트 실행

다양한 운영 체제에서 애플리케이션을 테스트하여 호환성을 확인한다.

```yaml
name: CI on Multiple OS

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ ubuntu-latest, windows-latest, macos-latest ]
        node-version: [ 14, 16, 18 ]

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: Node.js 설정
      uses: actions/setup-node@v3
      with:
        node-version: ${{ matrix.node-version }}

    - name: 종속성 설치
      run: npm install

    - name: 테스트 실행
      run: npm test
```

- 여러 운영 체제(Ubuntu, Windows, macOS)에서 테스트를 병렬로 실행.
- Node.js의 다양한 버전에서 애플리케이션의 호환성 테스트 수행.

### Docker 이미지 빌드 및 푸시

Docker 이미지를 빌드하고 Docker Hub에 푸시하여 배포를 자동화한다.

```yaml
name: Docker Build and Push

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: Docker 로그인
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}

    - name: Docker 이미지 빌드
      run: docker build -t myapp:${{ github.sha }} .

    - name: Docker 이미지 푸시
      run: docker push myapp:${{ github.sha }}
```

- Docker Hub에 로그인하여 이미지를 푸시.
- 커밋 해시를 태그로 사용하여 고유한 이미지 생성.
- 빌드한 Docker 이미지를 Docker Hub에 업로드.

### AWS에 애플리케이션 배포

AWS Elastic Beanstalk에 애플리케이션을 배포한다.

```yaml
name: Deploy to AWS

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: AWS 설정
      uses: aws-actions/configure-aws-credentials@v2
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-east-1

    - name: 애플리케이션 압축
      run: zip -r myapp.zip .

    - name: 애플리케이션 버전 생성
      run: |
        aws elasticbeanstalk create-application-version --application-name my-app --version-label ${{ github.sha }} --source-bundle S3Bucket=my-bucket,S3Key=myapp.zip

    - name: Elastic Beanstalk 환경 업데이트
      run: |
        aws elasticbeanstalk update-environment --environment-name my-env --version-label ${{ github.sha }}
```

- AWS 자격 증명을 설정하여 AWS 서비스에 접근.
- 애플리케이션을 압축하여 S3에 업로드.
- Elastic Beanstalk 환경을 업데이트하여 새로운 버전 배포.

### 코드 린트 및 포맷 검사

코드의 품질을 유지하기 위해 린트와 포맷 검사를 자동화한다.

```yaml
name: Lint and Format

on:
  pull_request:
    branches: [ main ]

jobs:
  lint:
    runs-on: ubuntu-latest

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: Node.js 설정
      uses: actions/setup-node@v3
      with:
        node-version: '16'

    - name: 종속성 설치
      run: npm install

    - name: ESLint 실행
      run: npm run lint

    - name: Prettier 실행
      run: npm run format:check
```

- ESLint를 사용하여 코드의 문법 및 스타일 검사.
- Prettier를 사용하여 코드 포맷 검사.
- Pull Request 생성 시 자동으로 린트와 포맷 검사 실행.

### 패키지 퍼블리싱

npm 패키지를 자동으로 배포한다.

```yaml
name: Publish Package

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  publish:
    runs-on: ubuntu-latest

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: Node.js 설정
      uses: actions/setup-node@v3
      with:
        node-version: '16'
        registry-url: 'https://registry.npmjs.org/'

    - name: npm 로그인
      run: echo "//registry.npmjs.org/:_authToken=${{ secrets.NPM_TOKEN }}" > ~/.npmrc

    - name: 패키지 빌드
      run: npm run build

    - name: 패키지 퍼블리싱
      run: npm publish
```

- 태그가 `v*.*.*` 형식으로 푸시될 때 패키지 빌드 및 퍼블리싱 수행.
- npm 레지스트리에 로그인하여 패키지 업로드.
- 퍼블리싱 전에 패키지 빌드 실행.

### Slack 알림 통합

빌드 상태를 Slack 채널에 알림으로 전송한다.

```yaml
name: CI with Slack Notification

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: Node.js 설정
      uses: actions/setup-node@v3
      with:
        node-version: '16'

    - name: 종속성 설치
      run: npm install

    - name: 테스트 실행
      run: npm test

    - name: Slack 알림
      if: always()
      uses: slackapi/slack-github-action@v1.23.0
      with:
        payload: |
          {
            "text": "빌드 상태: ${{ job.status }}"
          }
      env:
        SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
```

- 빌드 작업이 완료되면 Slack에 빌드 상태를 알림.
- `if: always()`를 사용하여 성공 또는 실패 여부에 관계없이 알림 전송.
- Slack Bot Token을 사용하여 인증.

### 캐시 활용한 빌드 속도 개선

종속성 캐시를 활용하여 빌드 시간을 단축한다.

```yaml
name: CI with Caching

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: 캐시 복원
      uses: actions/cache@v3
      with:
        path: ~/.npm
        key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
        restore-keys: |
          ${{ runner.os }}-node

    - name: Node.js 설정
      uses: actions/setup-node@v3
      with:
        node-version: '16'

    - name: 종속성 설치
      run: npm ci

    - name: 테스트 실행
      run: npm test
```

- `actions/cache`를 사용하여 `~/.npm` 디렉토리의 종속성을 캐시.
- `npm ci` 명령을 사용하여 종속성을 설치, 캐시를 활용하여 설치 속도 향상.
- 캐시 키는 운영 체제와 `package-lock.json`의 해시를 기반으로 설정.

### GitHub Pages에 정적 사이트 배포

정적 웹사이트를 GitHub Pages에 자동으로 배포한다.

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3
      with:
        persist-credentials: false

    - name: Node.js 설정
      uses: actions/setup-node@v3
      with:
        node-version: '16'

    - name: 종속성 설치
      run: npm install

    - name: 빌드
      run: npm run build

    - name: Pages에 배포
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./dist
```

- 코드 체크아웃 시 자격 증명 유지 비활성화.
- 종속성을 설치하고 빌드 실행.
- 빌드된 파일을 GitHub Pages에 배포.

### 데이터베이스 마이그레이션 자동화

배포 시 데이터베이스 마이그레이션을 자동으로 수행한다.

```yaml
name: Deploy with DB Migration

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: Node.js 설정
      uses: actions/setup-node@v3
      with:
        node-version: '16'

    - name: 종속성 설치
      run: npm install

    - name: 빌드
      run: npm run build

    - name: 배포
      run: ./deploy.sh

    - name: 데이터베이스 마이그레이션
      run: npm run migrate
```

- 배포 스크립트 실행 후 데이터베이스 마이그레이션 수행.
- 배포와 마이그레이션을 하나의 워크플로우에서 자동화.

### 커스텀 액션 사용

커스텀 액션을 사용하여 특정 작업을 수행한다.

```yaml
name: Custom Action Workflow

on:
  push:
    branches: [ main ]

jobs:
  custom:
    runs-on: ubuntu-latest

    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v3

    - name: 커스텀 액션 실행
      uses: ./actions/my-custom-action
      with:
        input1: 'value1'
        input2: 'value2'
```

- 로컬에 정의된 커스텀 액션 `./actions/my-custom-action`을 사용.
- 입력 파라미터를 전달하여 커스텀 작업 수행.
- 커스텀 액션은 프로젝트 내에서 재사용 가능.

## GitHub Actions의 한계와 해결 방안

1. **러너의 자원 제한**
    - GitHub 호스팅 러너는 CPU, 메모리 등의 자원 제한이 있다. 이를 해결하기 위해 자체 호스팅 러너를 설정하여 자원을 확장할 수 있다.
    - 또한, 워크플로우를 최적화하여 빌드 시간을 줄이는 것도 중요한 전략이다.
2. **로그 관리의 복잡성**
    - 워크플로우가 복잡해질수록 로그를 추적하고 디버깅하는 데 어려움이 발생할 수 있다. 이를 해결하기 위해 로그를 잘 관리하고, 오류 발생 시 Slack과 같은 툴과 통합하여 실시간 알림을 받을 수 있다.
3. **비용 관리**
    - 무료 제공 범위를 넘어서면 GitHub Actions의 사용 비용이 발생할 수 있다. 이를 방지하기 위해 워크플로우 실행을 최적화하거나, 자체 호스팅 러너를 이용하여 비용을 절감할 수 있다.