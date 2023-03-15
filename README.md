# Unreal Asset Duplicator

# ue-asset-duplicator

This scripts duplicates selected Unreal assets multiple times.

# Requirements

* Unreal Engine 4.26 or later installed
* Python 3.7 or later installed
* PyQt5 module installed

# Installation
1. Clone this repository or download the ZIP archive and extract its contents.
2. Copy and paste it into your Unreal Engine projects script file.

# Usage
1. Select one or more assets in the Content Browser.
2. Go to **File > Execute Python Script**
3. Locate your script in your project's files and run it.

# Notes
* The tool will create as many copies as you select. You can change this value by modifying the ```num_copies``` variable in the script.
* The duplicated assets will be named using the format ```original_name_0```, ```original_name_1```, etc. You can change this format by modifying the ```new_name``` variable in the script.
