import sys
from datetime import date

if len(sys.argv) == 2:
    new_version = sys.argv[1]
    
    with open("version.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    lines[0] = new_version
    with open("version.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)
    
    with open("main.py", "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line_index in range(len(lines)):
        if "#the version must be changed for every release" in lines[line_index]:
            lines[line_index] = "        app.setApplicationVersion(\"" + new_version + "\") #the version must be changed for every release\n"
            break
    with open("main.py", "w", encoding="utf-8") as file:
        file.writelines(lines)
    
    with open("windows/create_windows_installer.iss", "r", encoding="utf-8") as file:
        lines = file.readlines()
    lines[4] = "#define MyAppVersion \"" + new_version + "\"\n"
    with open("windows/create_windows_installer.iss", "w", encoding="utf-8") as file:
        file.writelines(lines)
    
    #no version number to update in mac directory
    
    with open("ubuntu/BEM-File-Editor/DEBIAN/control", "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line_index in range(len(lines)):
        if "Version: " in lines[line_index]:
            lines[line_index] = "Version: " + new_version + "\n"
            break
    with open("ubuntu/BEM-File-Editor/DEBIAN/control", "w", encoding="utf-8") as file:
        file.writelines(lines)
    
    with open("ubuntu/BEM-File-Editor/usr/share/applications/BEM-File-Editor.desktop", "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line_index in range(len(lines)):
        if "Version=" in lines[line_index]:
            lines[line_index] = "Version=" + new_version + "\n"
            break
    with open("ubuntu/BEM-File-Editor/usr/share/applications/BEM-File-Editor.desktop", "w", encoding="utf-8") as file:
        file.writelines(lines)
    
    with open("run with python in console/instructions.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line_index in range(len(lines)):
        if "use \"python main.py\" to run the BEM File Editor " in lines[line_index]:
            lines[line_index] = "use \"python main.py\" to run the BEM File Editor " + new_version + "\n"
            break
    with open("run with python in console/instructions.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)
    
    with open("README.md", "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line_index in range(len(lines)):
        if "## Version" in lines[line_index]:
            lines[line_index] = "## Version " + new_version + "\n"
        elif "Windows 11 x86_64 [BEM-File-Editor-Setup.exe]" in lines[line_index]:
            lines[line_index] = "Windows 11 x86_64 [BEM-File-Editor-Setup.exe](https://github.com/BEMinstructionals/BEMinstructionals.github.io/releases/download/v" + new_version + "/BEM-File-Editor-Setup.exe)\n"
        elif "macOS Sequoia ARM64 [BEM-File-Editor.dmg]" in lines[line_index]:
            lines[line_index] = "macOS Sequoia ARM64 [BEM-File-Editor.dmg](https://github.com/BEMinstructionals/BEMinstructionals.github.io/releases/download/v" + new_version + "/BEM-File-Editor.dmg)\n"
        elif "Ubuntu 24.04.2 LTS amd64 [BEM-File-Editor.deb]" in lines[line_index]:
            lines[line_index] = "Ubuntu 24.04.2 LTS amd64 [BEM-File-Editor.deb](https://github.com/BEMinstructionals/BEMinstructionals.github.io/releases/download/v" + new_version + "/BEM-File-Editor.deb)\n"
        elif "Download [BEM-File-Editor-" in lines[line_index]:
            lines[line_index] = "Download [BEM-File-Editor-" + new_version + ".zip](https://github.com/BEMinstructionals/BEMinstructionals.github.io/releases/download/v" + new_version + "/BEM-File-Editor-" + new_version + ".zip)\n"
    with open("README.md", "w", encoding="utf-8") as file:
        file.writelines(lines)
    
    with open("docs/index.html", "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line_index in range(len(lines)):
        if "<!-- must be changed with each release -->" in lines[line_index]:
            lines[line_index] = "        <h3 style=\"padding-left: 2em;\" id=\"id_Installers\">Installers for Version " + new_version + "</h3><!-- must be changed with each release -->\n"
        elif "Windows 11 x86_64" in lines[line_index]:
            lines[line_index] = "          <p style=\"padding-left: 3em;\">Windows 11 x86_64 <a href=\"https://github.com/BEMinstructionals/BEMinstructionals.github.io/releases/download/v" + new_version + "/BEM-File-Editor-Setup.exe\" target=\"_blank\" style=\"text-decoration: underline; color: blue;\">BEM-File-Editor-Setup.exe</a></p>\n"
        elif "macOS Sequoia ARM64" in lines[line_index]:
            lines[line_index] = "          <p style=\"padding-left: 3em;\">macOS Sequoia ARM64 <a href=\"https://github.com/BEMinstructionals/BEMinstructionals.github.io/releases/download/v" + new_version + "/BEM-File-Editor.dmg\" target=\"_blank\" style=\"text-decoration: underline; color: blue;\">BEM-File-Editor.dmg</a></p>\n"
        elif "Ubuntu 24.04.2 LTS amd64" in lines[line_index]:
            lines[line_index] = "          <p style=\"padding-left: 3em;\">Ubuntu 24.04.2 LTS amd64 <a href=\"https://github.com/BEMinstructionals/BEMinstructionals.github.io/releases/download/v" + new_version + "/BEM-File-Editor.deb\" target=\"_blank\" style=\"text-decoration: underline; color: blue;\">BEM-File-Editor.deb</a></p>\n"
        elif "<p style=\"padding-left: 3em;\">Download <a" in lines[line_index]:
            lines[line_index] = "          <p style=\"padding-left: 3em;\">Download <a href=\"https://github.com/BEMinstructionals/BEMinstructionals.github.io/releases/download/v" + new_version + "/BEM-File-Editor-" + new_version + ".zip\" target=\"_blank\" style=\"text-decoration: underline; color: blue;\">BEM-File-Editor-" + new_version + ".zip</a></p>\n"
    with open("docs/index.html", "w", encoding="utf-8") as file:
        file.writelines(lines)
    
    with open("docs/sitemap.xml", "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line_index in range(len(lines)):
        if "<lastmod>" in lines[line_index]:
            lines[line_index] = "    <lastmod>" + date.today().isoformat() + "</lastmod>\n"
    with open("docs/sitemap.xml", "w", encoding="utf-8") as file:
        file.writelines(lines)

else:
    print("You must provide exactly one command line argument.")