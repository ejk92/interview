# -*- coding: utf-8 -*-


class Calculator(object):
    """Class for mathematical calculations saved as text"""

    # DEFINE OPERATOR CONSTANTS
    OPERATOR_PLUS = '+'
    OPERATOR_MINUS = '-'
    OPERATOR_MUL = '*'
    OPERATOR_DIV = '/'
    BRACKET_LEFT = '('
    BRACKET_RIGHT = ')'

    OPERATORS = [OPERATOR_PLUS, OPERATOR_MINUS, OPERATOR_MUL, OPERATOR_DIV]

    OPERATOR_WEIGHT = {
        OPERATOR_PLUS: 1,
        OPERATOR_MINUS: 1,
        OPERATOR_MUL: 2,
        OPERATOR_DIV: 2,
    }

    OPERATOR_MAPPER = {
        OPERATOR_PLUS: lambda x, y: x+y,
        OPERATOR_MINUS: lambda x, y: x-y,
        OPERATOR_MUL: lambda x, y: x*y,
        OPERATOR_DIV: lambda x, y: x/y,
    }

    @staticmethod
    def _get_number_from_string(x):
        """Try to retrieve number from expression element"""
        try:
            return float(x)
        except ValueError:
            raise ValueError('Unknown element')

    def __init__(self, expression=None):
        if expression is not None:
            self.set_expression(expression)

    def set_expression(self, expression):
        self._valid_expression(expression)
        self.expression = expression

    @staticmethod
    def _valid_expression(expression):
        NotImplemented

    def _calculate(self, a, b, operator):
        return self.OPERATOR_MAPPER[operator](a, b)

    def _get_postfix_notation(self):
        """
        Change infix to postfix notation of expression.
        Implementation of Shunting-Yard algorithm.

        :return: list of expression elements with postfix notation order
        """
        postfix, operators_stack = list(), list()  # initialize postfix list and auxiliary stack

        for element in self.expression.split():
            if element in self.OPERATORS:
                if operators_stack:
                    # while stack isn't empty and "stack top" is stronger(e.g. multiplication is stronger than addition)
                    # move "stack top" into postfix list
                    while operators_stack \
                            and operators_stack[-1] in self.OPERATORS \
                            and self.OPERATOR_WEIGHT[operators_stack[-1]] >= self.OPERATOR_WEIGHT[element]:
                        postfix.append(operators_stack.pop())

                operators_stack.append(element)

            elif element == self.BRACKET_LEFT:
                operators_stack.append(element)

            elif element == self.BRACKET_RIGHT:
                # searching for left bracket on stack, moving "stack Top" to postfix list
                while operators_stack and operators_stack[-1] != self.BRACKET_LEFT:
                    postfix.append(operators_stack.pop())
                operators_stack.pop()  # remove left bracket

            else:  # numbers always goes into postfix list
                postfix.append(self._get_number_from_string(element))

        if operators_stack:  # move others stack elements to postfix list
            postfix.extend(reversed(operators_stack))

        return postfix

    def resolve_expression(self):
        """
        Resolving expression in postfx notation.

        :return: number - result of computation
        """
        stack = list()

        for element in self._get_postfix_notation():
            if element in self.OPERATORS:  # get two elements from top of stack, push result of operation on stack
                operand_a = stack.pop()
                operand_b = stack.pop()
                value = self._calculate(operand_b, operand_a, element)
                stack.append(value)
            else:  # push to stack if number
                stack.append(element)

        return stack.pop()


if __name__ == '__main__':
    test_cases = [
        ('-1 * ( 2 * 6 / 3 )', -4),
        ('-1 * 2 + 3 + 6 * 2', 13),
        ('0 * 2 - 9 * 3 * 1', -27),
        ('-3 / 1 - 6 / 5 * 2', -5.4),
        ('-3 / ( 1 - 6 ) + 3 * 2', 6.6),
        ('0 * ( 2 - 9 ) + 5 * 3', 15),
        ('1 + 0 * ( ( 2 - 9 ) + 5 ) * 3', 1),
    ]

    calculator = Calculator()
    for expression, result in test_cases:
        calculator.set_expression(expression)
        outcome = calculator.resolve_expression()
        print 'Expression: {}, from test case: {}, from calculator: {}'.format(expression, result, outcome)
