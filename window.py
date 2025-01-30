import tkinter
from typing import Callable

WIDTH, HEIGHT = 800, 600
HSTEP, VSTEP = 13, 18


class Window:
    __window: tkinter.Tk
    __canvas: tkinter.Canvas
    __display_list: list[tuple[int, int, str]]
    __scroll: int
    __SCROLL_STEP: int

    def __init__(self):
        self.__window = tkinter.Tk()
        self.__canvas = tkinter.Canvas(self.__window, width=WIDTH, height=HEIGHT)
        self.__canvas.pack()
        self.__scroll = 0
        self.__SCROLL_STEP = 15

    def mainLoop(self) -> None:
        self.__window.mainloop()

    def setLayout(self, text: str) -> None:
        display_list = []
        cursor_x, cursor_y = HSTEP, VSTEP

        for character in text:
            display_list.append((cursor_x, cursor_y, character))
            cursor_x += HSTEP

            if cursor_x >= WIDTH - HSTEP:
                cursor_y += VSTEP
                cursor_x = HSTEP

        self.__display_list = display_list

    def draw(self):
        self.__canvas.delete("all")
        for x, y, character in self.__display_list:
            if y > self.__scroll + HEIGHT:
                continue
            if y + VSTEP < self.__scroll:
                continue

            self.__canvas.create_text(x, y - self.__scroll, text=character)

    def scrollDown(self):
        self.__scroll += self.__SCROLL_STEP
        self.draw()
    
    def scrollUp(self):
        if self.__scroll - self.__SCROLL_STEP >= 0:
            self.__scroll -= self.__SCROLL_STEP

        if self.__scroll < 0:
            self.__scroll = 0

        self.draw()

    def bind(self, event: str, handle: Callable[[tkinter.Event], None]):
        self.__window.bind(event, handle)
