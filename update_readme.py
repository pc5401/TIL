import os

readme_contents = "# Today I Learned\n\n"

for root, dirs, files in os.walk("TIL"):
    dirs.sort()
    print("Visiting:", root)  # 현재 방문 중인 폴더 출력
    if "README.md" in files:
        path = os.path.relpath(root, "TIL").replace(os.sep, '/')
        readme_contents += f"- [{path}]({root}/README.md)\n"
        print("Added to README:", path)  # README에 추가된 항목 출력

with open("README.md", "w") as f:
    f.write(readme_contents)
