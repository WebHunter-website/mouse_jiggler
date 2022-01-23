# Mouse jiggler

## About
Mouse jiggler is an script which purpose is to periodically move mouse cursor to top left corner of the screen. This is done to keep computer system active in case, for example, company managed system does not allow to disable system lock timer.

Script checks cursor position every 5 minutes. If position is different than remembered than new position is memorized. If after 5 minutes cursor position is the same as remembered script will move cursor to top left corner and bact to starting position. In this mode script checks mouse position every 60 seconds.

The way the script works allows to prevent system lock, keeps **Teams** status **Available**, and so on.

## Requirements
  * Python 3+

## Setup
Recommended way to use `mouse_jiggler` is to create Python virtual environment:
```
python -m venv .\venv
```
and install project required packages:
```
.\venv\Scripts\python.exe -m pip install -r .\requirements.txt
```

## Usage
To use `mouse_jiggler` simply open terminal and run:
```
.\venv\Scripts\python.exe ./mouse_jiggler.py
```