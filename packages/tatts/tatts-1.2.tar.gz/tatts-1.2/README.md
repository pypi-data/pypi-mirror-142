[![PyPI](https://img.shields.io/pypi/v/tatts?label=stable%20eversion&style=for-the-badge)](https://pypi.org/project/tatts/)

[![PyPI](https://img.shields.io/pypi/l/tatts?style=for-the-badge)](https://choosealicense.com/licenses/mit/)


# tatts

this project is a python package that uses google translate to read text (tts) and to translate!

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tatts.

```bash
pip install tatts
```

## Usage

```python
import tatts

# text to speak
tatts.speak("hello world!")

# returns a translated text to whatever language you want
tatts.translate("hello world!",'en')
```


**notice that if you don't have chrome driver in path/folder that you running the python code from the package will auto-install the chromedriver.exe**

**it will show you a dialog that asks you to install the chrome driver 
and if you say y (yes) it will install the last stable version of chrome driver**


## License
[mit](https://choosealicense.com/licenses/mit/)
