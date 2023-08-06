# gcode2zaxe

A CLI that converts gcode files to Zaxe print ready file. You can use it from the command line after installing it. Executable name is `gcode2zaxe`.

## Installation

Run:&nbsp; ``pip install gcode2zaxe``

## Usage

* Show help: ``gcode2zaxe -h``

* Convert gcode file to Zaxe print ready file: ``gcode2zaxe -g input.gcode -o output.zaxe``

## Parameters

* ``-h, --help:`` Show help.

* ``-p, --path:`` Path to the image or folder to optimize. Defaults to the current directory if not specified.

* ``-r, --recursive:`` Optimize all images in a folder recursively. Defaults to False if not specified.

* ``-n, --number:`` Optimize a number of images. Defaults to all images in the folder if not specified.

* ``-q, --quality:`` Optimize with custom quality. Defaults to 80 if not specified.

## Important notes

* BACKUP YOUR IMAGES BEFORE OPTIMIZING! All images will be overwritten with optimized versions.

* This is a simple CLI application. It is not meant to be a full-featured image optimizer.

* Relative and absolute paths are supported.

* The quality parameter is a value between 0 and 100.

* The number parameter is a positive integer. And is not required.