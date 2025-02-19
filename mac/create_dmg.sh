#!/bin/bash

rm -r build
rm -r dist
rm -r env
rm -r "BEM File Editor"
rm "BEM File Editor.dmg"
cp ../LICENSE.txt LICENSE.txt
cp ../version.txt version.txt
python3 -m venv env
env/bin/pip3 install pyside6 pyinstaller
env/bin/pyinstaller mac.spec
rm -r "dist/BEM File Editor"
ln -s /Applications dist/Applications
mv dist "BEM File Editor"
hdiutil create -format UDZO "BEM File Editor.dmg" -srcfolder "BEM File Editor"
rm -r "BEM File Editor"
rm -r build
rm -r env
rm LICENSE.txt
rm version.txt
