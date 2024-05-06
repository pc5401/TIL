# github 트러블슈팅

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
