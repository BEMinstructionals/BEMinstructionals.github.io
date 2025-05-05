# BEM File Editor

The BEM File Editor is a modern editor for *.idf files, which are the Input Data File (IDF) files for the [EnergyPlus](https://energyplus.net/) whole building energy simulation program. The BEM File Editor installer does not contain any version of the EnergyPlus simulation program. Each version of EnergyPlus you want to use must be installed separately.

## Version 1.0.0

### Installers

Windows 11 x86_64 [BEM-File-Editor-Setup.exe](https://github.com/BEMinstructionals/BEMinstructionals.github.io/releases/download/v1.0.0/BEM-File-Editor-Setup.exe)

macOS Sequoia ARM64 [BEM-File-Editor.dmg](https://github.com/BEMinstructionals/BEMinstructionals.github.io/releases/download/v1.0.0/BEM-File-Editor.dmg)

Ubuntu 24.04.2 LTS amd64 [BEM-File-Editor.deb](https://github.com/BEMinstructionals/BEMinstructionals.github.io/releases/download/v1.0.0/BEM-File-Editor.deb)

### Run using Python

If you want to run the BEM File Editor without installing it, you can run the main.py file with python. I recommend using venv to create a python virtual environment that uses Python 3.12.9 for compatibility and install the pyside6 package with pip. Then python main.py will start the BEM File Editor. Keep in mind this will be slower since the installer is optimized.

### Reporting Bugs or Annoying Behavior

I have tested on Windows 11 x86_64, but I suspect there are still some bugs and annoying behavior. If you encounter a bug, you can try viewing the console output by enabling the View->Application Settings "Show Python Console Tab" checkbox. If there is no exception thrown then I probably made a logical error in the code, in which case all you'll see in the "python console" tab is datetimes of when the BEM File Editor was opened. In both cases, please document the steps to reproduce the behavior, [create an issue on GitHub](https://github.com/BEMinstructionals/BEMinstructionals.github.io/issues), and I will try to fix it.

## Licenses

The BEM File Editor main.py code is licensed under a BSD-3-Clause license. See the [LICENSE](https://github.com/BEMinstructionals/BEMinstructionals.github.io/blob/master/LICENSE.md) file for details.

The BEM Instructionals logo is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) license.

PySide6 is licensed under the [GNU Lesser General Public License version 3](https://www.gnu.org/licenses/lgpl-3.0.en.html#license-text).

## Acknowledgments

The BEM File Editor was inspired by the [IDF+ Editor](https://github.com/mattdoiron/idfplus) created by Matt Doiron.

A big Thank You! to all users who document and report bugs and annoying behavior when they occur.
