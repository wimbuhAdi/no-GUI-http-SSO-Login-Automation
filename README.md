# no-GUI-http-SSO-Login-Automation
--
python browser automation using pyppeteer v0.0.25 (headless chromium automation library) to automate login policy in order to joint UGM University Network

##Testing Enviroment
tested on python3.7 (faceing dificulties with 2.7 and 3.5) running on cloud ubuntu 16.04

###installation (coppy of pypi.org)
Pyppeteer requires python 3.6+. (experimentally supports python 3.5)
Install by pip from PyPI:
```
python3 -m pip install pyppeteer
```
Or install latest version from github:
```
python3 -m pip install -U git+https://github.com/miyakogi/pyppeteer.git@dev
```
You and add other functionality to your automation project using provided pyppeteer API which is puppeteer alternative for python development

##Complite API documentation
reading material is available on official [Puppetier devlopment website] (https://pptr.dev/) and [pyppeteer documentation] (https://pypi.org/project/pyppeteer/)

```
From my understanding that the pyppeteer using asyncio-await to make sure the chromium process is finish before next command line is executed, this make sure the element on the web page that the program want to interract is present (so wouldn't throw element not found error)
```
