# github 트러블슈팅

### 목차

[GitHub Actions 경로 설정 문제 해결](gitHub-actions-경로-설정-문제-해결)
[gist README 이미지 업로드](gist-readme-이미지-업로드)
[GitHub Actions UnicodeDecodeError 에러](#github-actions-unicodedecodeerror-에러)

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

---

## gist README 이미지 업로드

- 기간 : 2024-06-30 ~ 2024~07-01

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

---

## GitHub Actions UnicodeDecodeError 에러

### 문제 상황

- 기간: 2024-07-03 ~ 2024-07-05
- TIL을 시작하고 README.md를 자동으로 작성하고 싶어서 Python 스크립트와 GitHub Actions을 구축함.
- GitHub Actions 워크플로우가 실행되었으나 `UnicodeDecodeError`로 인해 스크립트가 실패함.

### 원인

- `update_readme.py` 스크립트가 특정 파일을 UTF-8로 읽는 도중 예상치 못한 바이트 시퀀스를 만나 `UnicodeDecodeError`가 발생함.
- 파일 인코딩 문제로 인해 스크립트가 중단됨.

### 해결 방법

- 스크립트에서 파일을 읽을 때 인코딩 오류를 처리하도록 예외 처리를 추가함.
- `get_md_title` 함수에 `UnicodeDecodeError` 예외 처리를 추가하여 오류가 발생하면 "Unknown Title"을 반환하고 로그에 기록하도록 수정함.
- `main` 함수에서 `README.md` 파일을 UTF-8 인코딩으로 작성하도록 수정함.

```js
import os
import logging

logging.basicConfig(level=logging.INFO)

def get_md_title(file_path: str) -> str:
    """마크다운 파일에서 첫 줄의 제목을 추출한다."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            first_line = file.readline().strip()
            if first_line.startswith('#'):
                return first_line.lstrip('#').strip()  # 제목에서 '#' 기호를 제거하고 반환
            else:
                return os.path.basename(file_path)  # 제목이 없는 경우 파일 이름 반환
    except UnicodeDecodeError:
        logging.error(f"Could not decode file: {file_path}")
        return "Unknown Title"

def write_content(path: str, cnt: int):
    content = ''
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    for dir in dirs:
        dir_path = f"{path}/{dir}".replace("\\", "/")  # 윈도우에서도 호환되는 경로 생성
        content += f'{"#" * cnt} [{dir}]({dir_path})\n'
        content += write_content(os.path.join(path, dir), cnt+1)

    for filename in files:
        file_path = f"{path}/{filename}".replace("\\", "/")  # 윈도우에서도 호환되는 경로 생성
        content += f'- [{get_md_title(os.path.join(path, filename))}]({file_path})\n'

    return content

def main():
    logging.info("Starting script...")
    readme_contents = "# Today I Learned\n\n\n"
    root_dir = "./learn"
    readme_contents += write_content(root_dir, 2)
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_contents)
    logging.info("README.md updated successfully.")

if __name__ == "__main__":
    main()

```

### 배운 점

- 파일 인코딩 문제는 예상치 못한 오류를 발생시킬 수 있으므로, 항상 예외 처리를 통해 안전하게 처리해야 함.
- GitHub Actions에서 발생하는 오류를 로그를 통해 파악하고 문제를 해결하는 과정의 중요성을 깨달음.
- 스크립트 수정 후, GitHub Actions가 정상적으로 작동하여 README.md 파일이 성공적으로 업데이트됨.
