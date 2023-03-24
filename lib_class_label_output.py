from tkinter import Label


class TextObj(Label):
    text_start_h = 50
    text_start_w = 340
    wind_start_space_x = 0
    wind_start_space_y = 0

    font_h = 30

    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg='white')
        self.config(padx=5)
        self.config(pady=5)
        self.config(anchor='e')
        self.config(font=("", self.font_h))

    def display_output_field(self):
        self.place(x=0, y=0, width=self.text_start_w, height=self.text_start_h)

    def output_in_output_field(self, f_calc):
        print(*f_calc.expression, f_calc.answer)
        if f_calc.answer == '':
            exit_text = "".join(f_calc.expression)
        else:
            exit_text = f_calc.answer
        if len(exit_text) > 15:
            exit_text = exit_text[:15]
        self.config(text=exit_text)


if __name__ == '__main__':
    print('Это библиотека, а не исполняемый код')
