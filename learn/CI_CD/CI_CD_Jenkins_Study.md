
# CI/CD란 무엇인가?

CI (Continuous Integration)는 여러 개발자들의 코드를 지속적으로 통합하여 빠르게 배포하는 과정이다. CI는 각 개발자가 작성한 코드를 자주 통합함으로써 코드 충돌을 방지하고, 문제를 조기에 발견하여 수정할 수 있게 한다. CI의 핵심은 자동화된 빌드와 테스트를 통해 코드가 언제나 배포 가능한 상태로 유지되도록 하는 것이다.

CD에는 두 가지 개념이 있다. 첫 번째는 **Continuous Delivery**로, 코드 베이스를 항상 배포 가능한 상태로 유지하며, 지속적으로 사용자에게 서비스를 제공하는 것을 목표로 한다. 이는 배포가 수동으로 이루어지지만, 코드가 언제든지 배포 가능한 상태로 준비되어 있다는 의미이다.

두 번째는 **Continuous Deployment**로, Continuous Delivery의 연장선에서 코드 변경 사항이 자동으로 배포되는 과정을 말한다. 이 과정에서는 모든 배포가 자동으로 이루어져 개발에서 배포까지의 과정이 완전히 자동화된다.

## CI/CD의 장점

- **빠른 피드백**: 코드 변경 시 즉각적인 빌드와 테스트를 통해 문제를 신속하게 발견하고 수정할 수 있다.
- **높은 품질**: 자동화된 테스트와 지속적인 통합으로 코드의 품질을 유지하고 향상시킬 수 있다.
- **효율성 증대**: 수동 작업을 줄이고 자동화를 통해 개발 및 배포 과정을 효율적으로 관리할 수 있다.
- **빠른 배포**: 자동화된 배포 파이프라인을 통해 새로운 기능과 수정 사항을 빠르게 사용자에게 제공할 수 있다.
- **리스크 감소**: 작은 단위로 지속적으로 배포함으로써 대규모 배포 시 발생할 수 있는 리스크를 줄일 수 있다.

# CI/CD 도구 비교

- **Jenkins**: 오픈 소스, 높은 커스터마이징 가능성, 풍부한 플러그인 생태계.
- **GitLab CI/CD**: GitLab과의 통합, 간편한 설정, DevOps 전체 프로세스 지원.
- **CircleCI**: 클라우드 기반, 빠른 설정, 병렬 빌드 지원.
- **Travis CI**: GitHub과의 쉬운 통합, 간단한 설정 파일.
- **Azure DevOps**: Microsoft 생태계와의 통합, 강력한 엔터프라이즈 기능.

# 젠킨스란 무엇인가?

Jenkins는 Java 환경에서 동작하는 오픈 소스 자동화 서버로, 다양한 플러그인을 통해 CI/CD 파이프라인을 구축할 수 있다. Jenkins는 개발자들이 코드를 효율적으로 빌드하고 테스트하며 배포할 수 있도록 도와주는 도구이다. 주요 플러그인으로는 Credentials Plugin, Git Plugin, Pipeline Plugin, Docker Plugin 등이 있으며, 이를 통해 Jenkins의 기능을 확장하고 맞춤형 CI/CD 파이프라인을 설계할 수 있다.

# 젠킨스의 Pipeline

Pipeline은 Jenkins에서 CI/CD 파이프라인을 구현하기 위한 플러그인들의 집합이다. Jenkins Pipeline을 사용하면 코드 빌드, 테스트, 배포 과정을 자동화할 수 있으며, 이를 통해 개발 과정의 효율성을 극대화할 수 있다. Pipeline의 구성 요소로는 Agent, Post, Stage, Steps 섹션이 있으며, 각 섹션은 특정 역할을 수행한다. 

Jenkins Pipeline에는 두 가지 문법이 존재한다. **Declarative Pipeline**은 간단하고 직관적인 문법을 제공하여 일반적인 파이프라인 작업을 쉽게 설정할 수 있게 하며, **Scripted Pipeline**은 더 복잡한 작업을 처리할 수 있는 유연성을 제공한다.

# Pipeline 섹션의 상세 설명

- **Agent section**은 작업을 수행할 Jenkins 노드나 Docker 컨테이너를 지정하는 역할을 한다. 특정 작업이 어느 환경에서 실행될지를 정의할 수 있다.
- **Post section**은 각 단계 후 후속 작업을 정의하는 섹션이다. 작업 성공, 실패, 항상 실행 등 다양한 조건에 따라 후속 작업을 설정할 수 있다.
- **Stage section**은 작업을 카테고리로 구분하여 빌드, 테스트, 배포 등의 단계로 나누는 역할을 한다. 이를 통해 파이프라인의 각 단계를 명확하게 정의할 수 있다.
- **Steps section**은 각 스테이지 안에서의 구체적인 작업 단계를 정의한다. 이 섹션에서 스크립트나 쉘 명령어 등을 사용하여 세부적인 작업을 수행할 수 있다.

# Declarative 문법

Declarative 문법은 Jenkins Pipeline에서 간결하고 이해하기 쉬운 구조로 파이프라인을 정의할 수 있게 한다. 주요 요소로는 **Environment**, **Stage**, **Options**, **Parameters**, **Triggers**, **When** 등이 있으며, 각 요소는 특정한 작업을 수행하거나 조건을 설정하는 데 사용된다. 이러한 요소들을 활용하여 각 스테이지에서 수행할 작업을 상세하게 정의할 수 있다.

## Declarative Pipeline 예제

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'make build'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'make test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'make deploy'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
```
# Jenkins 실습

Jenkins를 설치하고, 기본적인 파이프라인 예제를 통해 CI/CD 파이프라인을 구축하는 과정은 Jenkins 사용의 첫 걸음이다. Jenkins 설치 후 간단한 파이프라인을 설정하여 빌드와 배포 과정을 자동화하는 실습을 통해 Jenkins의 강력한 기능을 직접 체험할 수 있다. 이러한 실습을 통해 CI/CD 파이프라인의 개념을 구체적으로 이해하고, 실무에 적용할 수 있는 역량을 키울 수 있다.
