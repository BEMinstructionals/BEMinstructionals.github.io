#!/bin/bash

rm -r build
rm -r dist
rm -r env
rm -r "BEM-File-Editor/opt/BEM File Editor"
rm BEM-File-Editor.deb
cp ../LICENSE.md LICENSE.md
cp ../PySide6_license.txt PySide6_license.txt
cp ../version.txt version.txt
cp ../_internal/three_geometry.html three_geometry.html
cp -r ../_internal/three.js three.js
python3.14 -m venv env
env/bin/pip3.14 install pyside6 pyinstaller
env/bin/pyinstaller ubuntu.spec
mv "dist/BEM File Editor" "BEM-File-Editor/opt/BEM File Editor"
chmod -R 755 BEM-File-Editor
dpkg-deb --build BEM-File-Editor
rm -r build
rm -r dist
rm -r env
rm -r "BEM-File-Editor/opt/BEM File Editor"
rm LICENSE.md
rm PySide6_license.txt
rm version.txt
rm three_geometry.html
rm -r three.js
