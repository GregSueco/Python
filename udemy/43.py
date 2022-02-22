import math
import time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range (1000000):
    argument_list.append(i/10)

for formula in formulas_list:
    results_list = []
    formula_compiled = compile(formula,'internal variable','eval')
    print(formula)
    start_time = time.time()
    for x in argument_list:
        #print(x)
        result = eval(formula_compiled)
        #print(result)
        results_list.append(result)
    end_time = time.time()
    duration = end_time-start_time
    print(duration)
    max_element = max(results_list)
    min_element = min(results_list)
    print(max_element)
    print(min_element)