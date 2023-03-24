from lib_class_button import ButtonObj


class ButtonSimpleBlock:
    block_start_space_x = 0
    block_start_space_y = 50

    btn_smol_h = 50
    btn_smol_w = 50
    btn_large_h = 115
    btn_large_w = 50

    interval = 15

    buttons_block = ["7", "8", "9", "/", "CE",
                     "4", "5", "6", "*", "del",
                     "1", "2", "3", "-", "=",
                     ".", "0", "+/-", "+"]

    def __init__(self, parent, name_output_field, f_calc):
        x = self.block_start_space_x + self.interval
        y = self.block_start_space_y + self.interval
        for i in self.buttons_block:
            if i == "=":
                size_w = self.btn_large_w
                size_h = self.btn_large_h
            else:
                size_w = self.btn_smol_w
                size_h = self.btn_smol_h
            self.button_i = ButtonObj(parent, i)
            self.button_i.display_button(wind_start_space_x=x,
                                         wind_start_space_y=y,
                                         btn_start_h=size_h,
                                         btn_start_w=size_w)
            self.button_i.task_assignment(i, name_output_field, f_calc)
            x += size_w + self.interval
            if i == '=':
                size_h = size_h - self.btn_large_h + self.btn_smol_h
            if x == 180:
                x = 205
            if x > 285:
                x = 0 + self.interval
                y += size_h + self.interval


if __name__ == '__main__':
    print('Это библиотека, а не исполняемый код')
