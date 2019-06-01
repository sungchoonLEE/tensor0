from calculator.model import Calculator

if __name__ == '__main__':
    calc = Calculator(int(input("첫번째수 = ")), int(input("두번째수 = ")))
    print('{} + {} = {}'.format(calc.first, calc.second, calc.sum()))

