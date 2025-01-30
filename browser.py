from url import URL, lex
from window import Window


class Browser:
    __window: Window

    def __init__(self, window: Window):
        self.__window = window
        self.__window.bind("<Down>", lambda _: self.__window.scrollDown())
        self.__window.bind("<Up>", lambda _: self.__window.scrollUp())
        self.__window.bind(
            "<MouseWheel>",
            lambda e: (
                self.__window.scrollDown() if e.delta < 0 else self.__window.scrollUp()
            ),
        )

    def load(self, url: URL) -> None:
        req = url.request()
        self.__window.setLayout(lex(req))
        self.__window.draw()

    def mainLoop(self) -> None:
        self.__window.mainLoop()
