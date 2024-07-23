# 절대 경로 vs 상대 경로

## **절대 경로 (Absolute Path)**:

- **정의**: 파일 시스템에서 루트 디렉토리부터 시작하여 파일이나 디렉토리의 전체 경로를 나타냅니다.
- **형식**: UNIX 시스템에서는 `/`로 시작하고, Windows 시스템에서는 드라이브 문자를 포함합니다.
    - 예:
        - UNIX: `/home/user/documents/file.txt`
        - Windows: `C:\Users\user\documents\file.txt`
        - url : `https //www.naver.com`
- **특징**:
    - 위치 변경 시 영향을 받지 않음: 파일이나 디렉토리의 위치가 변경되어도 절대 경로는 동일하게 유지됩니다.
    - 서버 환경에서 주로 사용: 웹 서버나 파일 서버에서 리소스의 고정 위치를 지정할 때 사용됩니다.
- 예시:
    - **웹 서버 설정**: 웹 서버 설정 파일에서 고정된 리소스의 경로를 지정할 때 절대 경로를 사용 예) `DocumentRoot "/var/www/html"`
    - 파일 시스템 관리: 시스템 관리자가 스크립트를 작성할 때 특정 파일이나 디렉토리에 접근하기 위해 절대 경로를 사용 예) `cp /home/user/documents/report.txt /backup/reports/`

## **상대 경로 (Relative Path)**:

- **정의**: 현재 작업 디렉토리를 기준으로 파일이나 디렉토리의 경로를 나타냅니다.
- **형식**: 현재 디렉토리(`.`) 또는 상위 디렉토리(`..`)를 기준으로 경로를 작성합니다.
    - 예:
        - 하위 폴더: `images/picture.jpg`
        - 상위 폴더: `../documents/file.txt`
- **특징**:
    - 유연성: 프로젝트 내 파일 이동 시 상대 경로를 쉽게 수정할 수 있습니다.
    - 로컬 개발 환경에서 주로 사용: 웹 퍼블리싱이나 로컬 파일 탐색기에서 파일 경로를 지정할 때 사용됩니다.
- 예시:
    - **웹 개발**:HTML 파일에서 다른 리소스 (CSS, JS, 이미지 등)로의 링크를 설정할 때 상대 경로를 사용
    
    ```tsx
    <link rel="stylesheet" type="text/css" href="styles/main.css">
    <script src="scripts/app.js"></script>
    <img src="images/logo.png" alt="Logo">
    ```
    
    - **프로젝트 파일 구조**:프로젝트 내에서 파일을 참조할 때 상대 경로를 사용하여 파일의 위치를 쉽게 조정할 수 있다.