# GitHub Actions 소개

GitHub Actions는 GitHub에서 직접 코드를 자동화하고, CI/CD 작업을 처리할 수 있게 해주는 도구다. 이를 통해 소프트웨어 개발 워크플로우를 자동화하여, 소프트웨어 통합과 배포 과정을 간소화할 수 있다.

## GitHub Actions의 주요 기능

- **자동화된 워크플로우**: 소프트웨어 개발 및 배포 프로세스를 자동화한다.
- **다양한 이벤트에 대한 반응**: GitHub 저장소에서 발생하는 여러 이벤트(예: 푸시, 풀 리퀘스트, 이슈 생성 등)에 따라 작업을 트리거할 수 있다.
- **언어와 플랫폼에 구애받지 않음**: 다양한 운영 시스템에서 다양한 프로그래밍 언어와 도구를 지원한다.
- **재사용 가능한 컴포넌트**: 다른 사용자가 만든 Actions를 재사용하여 워크플로우를 빠르게 구성할 수 있다.

## GitHub Actions 구성 요소

1. **워크플로우(Workflows)**:
   
   - 워크플로우는 하나 이상의 작업을 포함하며, `.github/workflows` 디렉토리에 YAML 파일로 저장된다(or 작성한다).
   - 워크플로우는 지정된 이벤트에 의해 자동으로 실행.

2. **이벤트(Events)**:
   
   - 워크플로우는 저장소에서 발생하는 특정 이벤트에 의해 트리거 되는데
   - 예를 들어, `push`, `pull_request` 등의 이벤트이 있다.

3. **작업(Jobs)**:
   
   - 작업은 워크플로우 내에서 실행되는 일련의 단계로, 각 작업은 동일한 러너에서 또는 다른 러너에서 실행될 수 있다.

4. **단계(Steps)**:
   
   - 각 작업은 하나 이상의 단계로 구성됨.
   - 단계는 개별 명령이 실행되거나 다른 액션을 사용할 수 있다.

5. **액션(Actions)**:
   
   - 액션은 워크플로우에서 재사용할 수 있는 독립적인 명령 모듈이다.
   - 자체 액션을 생성하거나 GitHub 커뮤니티에서 공유된 액션을 사용할 수 있다.

6. **러너(Runners)**:
   
   - 러너는 GitHub Actions 워크플로우가 실행되는 서버.
   - GitHub은 호스팅된 러너를 제공하며, 사용자는 자신의 러너를 호스팅할 수도 있다.

## 결론(쓰는 이유)

GitHub Actions는 개발 팀이 소프트웨어 개발과정을 자동화하고, 보다 효율적으로 배포할 수 있도록 도와준다. 이 도구를 사용하면 복잡한 스크립트나 외부 서비스 없이도 깃허브 내에서 직접적인 자동화와 통합이 가능하다.



### 예시 (내 TIL repo 의 update-readme.yml 파일 참고)

```
name: Update README

on:  # 이 워크플로우가 언제 실행될지 정의
  push:
    branches:  # 특정 브랜치에 대한 푸시에서만 반응
      - master
    paths:  # 특정 경로의 파일들이 변경되었을 때만 반응
      - 'TIL/**'  

jobs:  # 작업 정의
  update-readme:  # 작업의 ID 및 이름
    runs-on: ubuntu-latest  # 작업이 실행될 환경
    steps:
      - uses: actions/checkout@v2  # GitHub 저장소를 체크아웃
      - name: Update README
        run: python update_readme.py  # Python 스크립트 실행
      - name: Commit and push if changed 
        run: |  # 다중 라인 스크립트 시작
          git config --global user.email "pc5401@naver.com"
          git config --global user.name "pc5401"
          git add README.md
          git commit -m "Update README" || exit 0
          git push


```
