# BEM File Editor

The BEM File Editor is a modern editor for *.idf files, which are the Input Data File (IDF) files for the [EnergyPlus](https://energyplus.net/) whole building energy simulation program. The BEM File Editor installers do not contain any version of the EnergyPlus simulation program. Each version of EnergyPlus you want to use must be installed separately.

The READMEs for GitHub repos have limited functionality and are meant to provide users with essential information, such as its purpose, usage, licenses, and access to the source code.

For a much more comprehensive overview, please see the accompanying [BEM Instructionals website](https://beminstructionals.com/) or the [BEM Instructionals YouTube Channel](https://www.youtube.com/@BEMInstructionals).

## Download Links

### Latest Release Installers and Standalone Code

The [Downloads](https://beminstructionals.com/#id_Downloads) section of the accompanying website has all the installers and files to run the BEM File Editor directly with Python for the latest version.

### Downloads for All Releases

If you would like to download the installers or release code for the current or a previous release directly from the GitHub repo, the [Releases page](https://github.com/BEMinstructionals/BEMinstructionals.github.io/releases) has all the releases and their assets.

## Reporting Bugs

### BEM File Editor

I have tested the most on Windows 11 because that is the OS I develop on, and I do test new features on macOS and Ubuntu, but I suspect there are still some bugs and annoying behaviors lurking in the code. If you encounter a bug in the BEM File Editor, you can try viewing the console output by enabling the View-&gt;Application Settings "Show Python Console Tab" checkbox. If there is no exception thrown, then I probably made a logical error in the code, in which case all you'll see in the "python console" tab is datetimes of when the BEM File Editor was opened. In both cases, please document the steps to reproduce the behavior, [create an issue on the BEM File Editor GitHub repo](https://github.com/BEMinstructionals/BEMinstructionals.github.io/issues), and I will try to fix it.

### EnergyPlus

EnergyPlus is completely separate from the BEM File Editor. If you think you've found a bug with one of the EnergyPlus programs, you can [create an issue on the EnergyPlus GitHub repo](https://github.com/NREL/EnergyPlus/issues).

## Licenses

The BEM File Editor main.py code is licensed under a BSD-3-Clause license. See the [LICENSE](https://github.com/BEMinstructionals/BEMinstructionals.github.io/blob/master/LICENSE.md) file for details.

The BEM Instructionals logo is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) license.

PySide6 is licensed under the [GNU Lesser General Public License version 3](https://www.gnu.org/licenses/lgpl-3.0.en.html#license-text).

## Acknowledgments

The BEM File Editor was inspired by the [IDF+ Editor](https://github.com/mattdoiron/idfplus) created by Matt Doiron.

A big Thank You! to all users who document and report bugs and annoying behavior when they occur.
