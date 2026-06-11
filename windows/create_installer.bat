rmdir /s /q build
rmdir /s /q dist
rmdir /s /q env
rmdir /s /q Output
copy ..\LICENSE.md LICENSE.md
copy ..\PySide6_license.txt PySide6_license.txt
copy ..\version.txt version.txt
copy ..\_internal\three_geometry.html three_geometry.html
xcopy ..\_internal\three.js three.js /E /I /H
python -m venv env
env\Scripts\pip3.exe install pyside6 pyinstaller
env\Scripts\pyinstaller.exe windows.spec
"C:\Program Files (x86)\Windows Kits\10\bin\10.0.26100.0\x64\signtool.exe" sign /a /tr http://timestamp.digicert.com /td sha256 /fd sha256 /n "Mitchal Dichter, LLC" "dist\main\BEM File Editor.exe"
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" "/Swindowssigntool=$qC:\Program Files (x86)\Windows Kits\10\bin\10.0.26100.0\x64\signtool.exe$q sign /a /tr http://timestamp.digicert.com /td sha256 /fd sha256 /n $qMitchal Dichter, LLC$q $f" create_windows_installer.iss
move "Output\BEM File Editor Setup.exe" "BEM-File-Editor-Setup.exe"
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q env
rmdir /s /q Output
del LICENSE.md
del PySide6_license.txt
del version.txt
del three_geometry.html
rmdir /s /q three.js
