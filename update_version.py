import sys, os

if len(sys.argv) == 2:
    new_version = sys.argv[1]
    
    with open('_internal/version.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    data[0] = new_version
    with open('_internal/version.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
    
    with open('windows/create_windows_installer.iss', 'r', encoding='utf-8') as file:
        data = file.readlines()
    data[4] = "#define MyAppVersion \"" + new_version + "\"\n"
    with open('windows/create_windows_installer.iss', 'w', encoding='utf-8') as file:
        file.writelines(data)
    
    with open('README.md', 'r', encoding='utf-8') as file:
        data = file.readlines()
    for line_index in range(len(data)):
        if "## Version" in data[line_index]:
            data[line_index] = "## Version " + new_version + "\n"
            break
    with open('README.md', 'w', encoding='utf-8') as file:
        file.writelines(data)
    
else:
    print("You must provide exactly one command line argument.")