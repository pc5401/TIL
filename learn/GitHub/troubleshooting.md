# github 트러블슈팅

### 목차

[GitHub Actions 경로 설정 문제 해결](gitHub-actions-경로-설정-문제-해결)

[gist README 이미지 업로드](gist-readme-이미지-업로드)

## GitHub Actions 경로 설정 문제 해결

### 문제 상황

- 기간 : 2024-05-03 ~ 2024~05-05
- TIL 을 시작하고 REASME.md를 작동으로 작성하고 싶어서 python 스크립트와 Github Actions 을 구축함.
- GitHub Actions 워크플로우에서 특정 디렉토리(`TIL/learn/**`)의 변경을 감지하도록 설정했으나, 워크플로우가 예상대로 트리거되지 않았음.

### 원인

- 경로 설정에 문제가 있었음. `TIL/learn/**` 대신 `learn/**`을 사용해야 했음. 이는 `.github/workflows` 폴더 기준으로 상대 경로를 설정해야 하기 때문임.

### 해결 방법

- `.yaml` 파일의 경로 설정을 `TIL/learn/**`에서 `learn/**`로 수정.

### 배운 점

- GitHub Actions에서 경로를 설정할 때는 항상 `.github/workflows` 디렉토리를 기준으로 상대 경로를 고려해야 한다는 점을 배움.
- 문제 해결 과정에서 경로 설정의 중요성을 다시 한번 인식하게 됨.





## gist README 이미지 업로드

원래

#### 원래 : GitHub Gist에 이미지 추가하기

1. 가장 간편한 방법 중 하나는 GitHub 이슈나 PR에 이미지를 업로드하는 것이다.

2. 이미지 URL 복사하기 이미지를 업로드한 후 해당 이미지의 URL을 복사한다.

3. Gist에서 이미지 링크 추가하기 Gist 파일을 열고 Markdown 형식을 사용하여 이미지 링크를 추가한다.

4. Markdown에서 이미지를 추가하는 기본 형식은 다음과 같다.

```md
![다이어그램](https://user-images.githubusercontent.com/yourusername/imagename.png)

```

### 문제 상황

- 원래 방법으로 했는데, gist 의 README 이미지가 깨졌다.

- 링크로는 제대로 이미지 창이 열렸지만, README에는 없었다.

### 원인 추측

- secret gist 여서 public 링크에 접속이 안 되나?(추측)

### 해결

- gist 하단의 comment 에 이미지 업로드 -> 링크 생성

- 해당 링크로 README 링크 교체

- 해결
