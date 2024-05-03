import os

readme_contents = "# Today I Learned\n\n"

for root, dirs, files in os.walk("."):
    dirs.sort()
    # "잡동사니" 제외
    if "잡동사니" in dirs:
        dirs.remove("잡동사니")

    if "README.md" in files:
        path = os.path.relpath(root, ".").replace(os.sep, '/')
        if "잡동사니" not in path.split('/'):
            readme_link = os.path.join(path, "README.md").replace(os.sep, '/')
            readme_contents += f"- [{path}]({readme_link})\n"

with open("README.md", "w") as f:
    f.write(readme_contents)