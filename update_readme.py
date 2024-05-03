import os

readme_contents = "# Today I Learned\n\n"

for root, dirs, files in os.walk("TIL"):
    dirs.sort()
    if "README.md" in files:
        path = os.path.relpath(root, "TIL").replace(os.sep, '/')
        readme_link = os.path.join(path, "README.md").replace(os.sep, '/')
        readme_contents += f"- [{path}]({readme_link})\n"

with open("README.md", "w") as f:
    f.write(readme_contents)
