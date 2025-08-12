import sys
from datetime import date

if len(sys.argv) == 3:
    new_version = sys.argv[1]
    old_version = sys.argv[2]
    
    filepaths = [
    "version.txt",
    "main.py",
    "windows/create_windows_installer.iss",
    "ubuntu/BEM-File-Editor/DEBIAN/control",
    "ubuntu/BEM-File-Editor/usr/share/applications/BEM-File-Editor.desktop",
    "run with python in console/instructions.txt",
    "docs/index.html",
    ]
    
    for filepath in filepaths:
        with open(filepath, "r", encoding="utf-8") as file:
            file_contents = file.read()
        updated_contents = file_contents.replace(old_string, new_string)
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(updated_contents)
    
    with open("docs/sitemap.xml", "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line_index in range(len(lines)):
        if "<lastmod>" in lines[line_index]:
            lines[line_index] = "    <lastmod>" + date.today().isoformat() + "</lastmod>\n"
    with open("docs/sitemap.xml", "w", encoding="utf-8") as file:
        file.writelines(lines)

else:
    print("You must provide exactly two command line arguments for the new_version and old_version in that order.")