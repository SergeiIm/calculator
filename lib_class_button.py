from lib_class_check_text import CheckPushButton


class ButtonObj(CheckPushButton):

    font = ("", 20)

    def __init__(self, parent, text='None'):
        super().__init__(parent)
        self.config(font=self.font, text=text)

    def task_assignment(self, name_button, name_output_field, f_calc):
        self.config(command=lambda i=name_button: self.push_the_button(i, name_output_field, f_calc))

    def display_button(self, wind_start_space_x=100, wind_start_space_y=100, btn_start_w=50, btn_start_h=50):
        self.place(x=wind_start_space_x,
                   y=wind_start_space_y,
                   width=btn_start_w,
                   height=btn_start_h)

    def push_the_button(self, name_button, name_output_field, f_calc):
        self.check_text(name_button, f_calc)
        if f_calc.flag:
            f_calc.count_result()
        name_output_field.output_in_output_field(f_calc)


if __name__ == '__main__':
    print('Это библиотека, а не исполняемый код')
