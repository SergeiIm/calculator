class Calc:
    def __init__(self):
        self.expression = ['']
        self.answer = ''
        self.flag = False

    def count_result(self):

        def is_number_to_float(f_text):
            try:
                f_result = float(f_text)
                return f_result
            except ValueError:
                return f_text

        def is_number_to_int(f_float):
            try:
                if f_float % 1 == 0:
                    return int(f_float)
                else:
                    return f_float
            except ValueError:
                return f_float

        result = self.expression.copy()

        for i in range(len(result)):
            result[i] = is_number_to_float(result[i])

        j = 0
        while j < len(result) - 1:
            if result[j] == "*" and type(result[j + 1]) == float and type(result[j - 1]) == float:
                result[j - 1] *= result[j + 1]
                del result[j]
                del result[j]

            elif result[j] == "/" and type(result[j + 1]) == float and type(result[j - 1]) == float:
                result[j - 1] /= result[j + 1]
                del result[j]
                del result[j]
            else:
                j += 1
            print(result)

        k = 0
        while k < len(result) - 1:
            if result[k] == "+" and type(result[k + 1]) == float and type(result[k - 1]) == float:
                result[k - 1] += result[k + 1]
                del result[k]
                del result[k]

            elif result[k] == "-" and type(result[k + 1]) == float and type(result[k - 1]) == float:
                result[k - 1] -= result[k + 1]
                del result[k]
                del result[k]
            else:
                k += 1
        self.answer = str(is_number_to_int(result[0]))
        self.flag = False
