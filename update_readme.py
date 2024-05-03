import os

readme_contents = "# Today I Learned\n\n"

for root, dirs, files in os.walk("TIL"):
    dirs.sort()
    # "잡동사니" 폴더를 제외하고 싶다면 아래와 같이 처리
    if "잡동사니" in dirs:
        dirs.remove("잡동사니")  # 목록에서 "잡동사니" 폴더 제거
    if "README.md" in files:
        path = os.path.relpath(root, "TIL").replace(os.sep, '/')
        if "잡동사니" not in path.split('/'):  # 경로에 "잡동사니"가 포함되지 않은 경우에만 추가
            readme_link = os.path.join(path, "README.md").replace(os.sep, '/')
            readme_contents += f"- [{path}]({readme_link})\n"

with open("README.md", "w") as f:
    f.write(readme_contents)