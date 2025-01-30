from browser import Browser
from window import Window
from url import URL

browser = Browser(Window())

if __name__ == "__main__":
    browser.load(URL("https://browser.engineering/examples/xiyouji.html"))
    browser.mainLoop()
