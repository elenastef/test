class Calculator(object):
    BUTTONS = '1234567890AB+-*/CDEF=#'

    def __init__(self):
        self._expression = ''

    def push(self, button):
        if button not in self.BUTTONS:
            raise CalculationError("Invalid button '%s'." % button)
        if button == 'A':
            button = '10'
        if button == 'B':
            button = '11'
        if button == 'C':
            button = '12'
        if button == 'D':
            button = '13'
        if button == 'E':
            button = '14'
        if button == 'F':
            button = '15'    
        if button == '=':
            self._expression = self._calculate(self._expression)
        elif button == '#':
            button = ' '
        else:
            self._expression += button
        return self._expression

    def _calculate(self, expression):
        try:
            return str(eval(expression))
        except SyntaxError:
            raise CalculationError('Invalid expression.')
        except ZeroDivisionError:
            raise CalculationError('Division by zero.')


class CalculationError(Exception):
    pass
