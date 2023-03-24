from tkinter import Button


class CheckPushButton(Button):

    def __init__(self, parent):
        super().__init__(parent)

    @staticmethod
    def check_text(f_text, f_calc):
        def checking_the_end_number(numb_in_str):
            if numb_in_str[-1] == ".":
                numb_in_str = numb_in_str[:-1]
            return numb_in_str

        def check_error(ff_calc):
            for i in range(len(ff_calc.expression)):
                if ff_calc.expression[i] == "/":
                    if float(ff_calc.expression[i + 1]) == 0:
                        ff_calc.flag = False
                        return

        dictionary_of_changes = {'period': ".", 'slash': '/', 'asterisk': '*', 'minus': '-', 'plus': '+'}
        if f_text in dictionary_of_changes:
            f_text = dictionary_of_changes[f_text]

        if f_text in "0123456789":
            if f_calc.expression[-1] != "0":
                f_calc.expression[-1] += f_text

        elif f_text == ".":
            if f_calc.expression[-1] == "0" or \
                    ("." not in f_calc.expression[-1] and len(f_calc.expression[-1]) > 0):
                f_calc.expression[-1] += f_text

        elif f_text in ('+', '-', '*', '/'):
            if f_calc.expression[-1] != "":
                f_calc.expression[-1] = checking_the_end_number(f_calc.expression[-1])
                f_calc.expression.append(f_text)
                f_calc.expression.append("")
            elif f_calc.expression[-1] == "" and len(f_calc.expression) > 1:
                f_calc.expression[-2] = f_text

        elif f_text == "+/-":
            if f_calc.expression[-1] != "":
                if float(f_calc.expression[-1]) != 0:
                    if f_calc.expression[-1][0] == "-":
                        f_calc.expression[-1] = f_calc.expression[-1][1:]
                    else:
                        f_calc.expression[-1] = "-" + f_calc.expression[-1]

        elif f_text == "del" or f_text == 'Delete':
            if f_calc.expression[-1] != "":
                f_calc.expression[-1] = f_calc.expression[-1][:-1]
            else:
                if len(f_calc.expression) > 2:
                    del f_calc.expression[-1], f_calc.expression[-1]

        elif f_text == "CE" or f_text == 'BackSpace':
            f_calc.expression.clear()
            f_calc.expression.append("")

        elif f_text == "=" or f_text == 'Return' or f_text == 'equal':
            if f_calc.expression[-1] != "":
                f_calc.flag = True
                check_error(f_calc)

        if f_text != "=" and f_calc.answer != "":
            f_calc.answer = ""

if __name__ == '__main__':
    print('Это библиотека, а не исполняемый код')