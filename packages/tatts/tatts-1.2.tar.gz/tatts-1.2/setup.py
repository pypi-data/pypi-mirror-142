from setuptools import setup, find_packages


long_description = open("README.md","r").read()

setup(
    name='tatts',
    version='1.2',
    license='MIT',
    author="ori299",
    author_email='email@example.com',
    packages=find_packages(),
    url='https://github.com/ORI299/ttast',
    keywords='tatts translate and tts text to speak',
    install_requires=[
          'selenium','colorama','scikit-learn','requests'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)