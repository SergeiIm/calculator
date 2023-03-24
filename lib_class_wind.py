from tkinter import Tk
from lib_class_btn_smpl_block import ButtonSimpleBlock, ButtonObj
from lib_class_label_output import TextObj
from lib_class_calc import Calc


class Window(Tk):
    wind_start_w = 340
    wind_start_h = 325
    wind_start_space_x = 100
    wind_start_space_y = 200
    wind_title = 'Калькулятор'
    wind_resizable_x = False
    wind_resizable_y = False

    def __init__(self):
        super().__init__()
        self.title(self.wind_title)
        self.resizable(self.wind_resizable_y, self.wind_resizable_x)
        self.geometry(self.return_geometry())

        self.calc = Calc()

        self.output_field = TextObj(self)
        self.output_field.display_output_field()

        self.block_one = ButtonSimpleBlock(self, self.output_field, self.calc)

        self.keyboard_button = ButtonObj(self)

        self.bind("<Key>", self.keyboard_input)

    @classmethod
    def return_geometry(cls):
        result = str(cls.wind_start_w) + "x" + str(cls.wind_start_h) + "+" + \
                 str(cls.wind_start_space_y) + "+" + str(cls.wind_start_space_x)
        return result

    def keyboard_input(self, event):
        a = event.keysym
        self.keyboard_button.push_the_button(a, self.output_field, self.calc)


if __name__ == '__main__':
    print('Это библиотека, а не исполняемый код')
