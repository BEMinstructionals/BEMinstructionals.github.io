rmdir /s /q build
rmdir /s /q dist
rmdir /s /q env
rmdir /s /q Output
copy ..\LICENSE.md LICENSE.md
copy ..\PySide6_license.txt PySide6_license.txt
copy ..\version.txt version.txt
python -m venv env
env\Scripts\pip3.exe install pyside6 pyinstaller
env\Scripts\pyinstaller.exe windows.spec
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" create_windows_installer.iss
move "Output\BEM File Editor Setup.exe" "BEM-File-Editor-Setup.exe"
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q env
rmdir /s /q Output
del LICENSE.md
del PySide6_license.txt
del version.txt