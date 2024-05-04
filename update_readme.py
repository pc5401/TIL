import os
import logging

logging.basicConfig(level=logging.INFO)

def get_md_title(file_path: str) -> str:
    """마크다운 파일에서 첫 줄의 제목을 추출한다."""
    with open(file_path, 'r', encoding='utf-8') as file:
        first_line = file.readline().strip()
        if first_line.startswith('#'):
            return first_line.lstrip('#').strip()  # 제목에서 '#' 기호를 제거하고 반환
        else:
            return os.path.basename(file_path)  # 제목이 없는 경우 파일 이름 반환


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
    with open('README.md', 'w') as f:
        f.write(readme_contents)


if __name__ == "__main__":
    main()