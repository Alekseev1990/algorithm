"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе.
"""


class PlatesStack:
    def __init__(self, max_plates):
        self.plates = [[]]
        self.max_plates = max_plates

    def __str__(self):
        return str(self.plates)

    def is_empty(self):
        return self.plates == [[]]

    def push_in(self, items):
        if len(self.plates[len(self.plates) - 1]) < self.max_plates:
            self.plates[len(self.plates) - 1].append(items)
        else:
            self.plates.append([])
            self.plates[len(self.plates) - 1].append(items)

    def pop_out(self):
        res = self.plates[len(self.plates) - 1].pop()
        if len(self.plates[len(self.plates) - 1]) == 0:
            self.plates.pop()
        return res

    def get_val(self):
        return self.plates[len(self.plates) - 1]

    def stack_size(self):
        plates_count = 0
        for stack in self.plates:
            plates_count += len(stack)
            return len(self.plates)

    def stack_count(self):
        return len(self.plates)


if __name__ == '__main__':
    p = PlatesStack(7)
    p.push_in('-')
    p.push_in('-')
    p.push_in('-')
    p.push_in('-')
    p.push_in('-')
    p.push_in('-')
    p.push_in('-')
    p.push_in('-')
    p.push_in('-')
    p.push_in('-')
    p.push_in('-')
    print(p)
