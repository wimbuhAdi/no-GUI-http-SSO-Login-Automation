'''
HI PAL, this python script run on python 3.6+ 
you need to setup the requrements as documented on https://github.com/wimbuhAdi/noGUI-httpLoginAutomation
WISH YOUR PROJECT GOES SMOOTHHHH.....
'''
import asyncio, time
from pyppeteer import launch

UNAME = "UsernameGoesHere"
PASSWORD = "literalyYourpassword"

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://internet.ugm.ac.id/')
    await page.click('body > div.px-content > div.col-lg-6.col-md-12.col-sm-12.col-xs-12.button-login > div > div:nth-child(1) > div > a.btn.btn-ugm.btn-lg.btn-block')
    await page.type('#username',UNAME)
    await page.type('#password',PASSWORD)
    await page.click('#fm1 > input.btn.btn-primary')
    print("Login SSO sucess as wimbuh.tri.hastomo")
    await asyncio.sleep(2)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
