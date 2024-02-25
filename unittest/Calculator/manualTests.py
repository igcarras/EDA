# This is a script containing tests as far as you know, which is fine but not super nice

from calculator import Calculator

calc = Calculator()

# Testing add
result = calc.add(5, 3) # resoult should be 8, so we check manually
print(result)

# Testing subtract
result = calc.subtract(5, 3) # resoult should be 2, so we check manually
print(result)
