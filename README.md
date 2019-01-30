# Test Task
This repository contains my solution to the task found at https://docs.google.com/document/d/1CoPMJ-vTboUOMPmETUhw1S61tIXuBmNLYwiHBK5109g/edit#

## Required installations
* Download and install Android SDK: https://developer.android.com/studio/
* Create an emulator using AVD manager: https://developer.android.com/studio/run/managing-avds. Android emulator version should be > 7.0.
* Download, install and run Appium: http://appium.io/
* Having Python3 installed with pip clone the repo and navigate to the root directory.
Install requirements: pip3 install requirements.txt
* Download the apk from http://files.slatestudio.com/sr82
* In the tests/pytest.ini file add an argument --apk with value == path to the apk on your computer. Eg 
```--apk=/Users/username/Downloads/Todoist_v12.8_apkpure.com.apk```

## How to run it
### By name:
```python3 -m pytest tests/test_task.py::TestTask::test_create_task_via_mobile_phone```
### By file name:
```python3 -m pytest tests/test_project.py```
### All tests:
```python3 -m pytest tests/```
