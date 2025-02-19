#!/bin/bash

rm -r build
rm -r dist
rm -r env
rm "BEM File Editor.tar.gz"
cp ../LICENSE.txt LICENSE.txt
cp ../_internal/version.txt version.txt
python3 -m venv env
env/bin/pip3 install pyside6 pyinstaller
env/bin/pyinstaller ubuntu.spec
cd dist
tar -zcvf "BEM File Editor.tar.gz" "BEM File Editor/"
cd ..
mv "dist/BEM File Editor.tar.gz" "BEM File Editor.tar.gz"
rm -r build
rm -r dist
rm -r env
rm LICENSE.txt
rm version.txt
