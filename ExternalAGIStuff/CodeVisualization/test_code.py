from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import obj
code = [
    "if input0.size == 1 and input1.size == 1:",
    "    return 'compare_single_digit_natural_numbers'(input0, input1)",
    "reg0 = input0.size",
    "reg1 = input1.size",
    "reg2 = 'compare_natural_numbers'(reg0, reg1)",
    "if reg2 == 'greater_than':",
    "    return 'greater_than'",
    "elif reg2 == 'less_than':",
    "    return 'less_than'",
    "for i in range(reg0):",
    "    reg3<i> = 'compare_single_digit_natural_number'('digit_to_number'(input0[i]), 'digit_to_number'(input1[i]))",
    "    if reg3<i> == 'greater_than':",
    "        return 'greater_than'",
    "    elif reg3<i> == 'less_than':",
    "        return 'less_than'",
    "return 'math_equal'"]

result = [[r['if'], ["AN EXPRESSION"], [r['return'], ["AN EXPRESSION"]], [], []],
[r['assign'], ["AN EXPRESSION"], ["AN EXPRESSION"]],
[r['assign'], ["AN EXPRESSION"], ["AN EXPRESSION"]],
[r['assign'], ["AN EXPRESSION"], ["AN EXPRESSION"]],
[r['if'], ["AN EXPRESSION"], [r['return'], ["AN EXPRESSION"]], [[["AN EXPRESSION"], [r['return'], ["AN EXPRESSION"]]]], []],
[r['for'], obj(0), ["AN EXPRESSION"], [r['assign'], ["AN EXPRESSION"], ["AN EXPRESSION"]],
[r['if'], ["AN EXPRESSION"], [r['return'], ["AN EXPRESSION"]], [[["AN EXPRESSION"], [r['return'], ["AN EXPRESSION"]]]], []]],
[r['return'], ["AN EXPRESSION"]]]
