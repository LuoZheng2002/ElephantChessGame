# input0: expression_for_constraint, input1: input1, input2: reg0
remove_one_element = '''
for i in range(input2.size):
    if 'func::solve_expression'(input0, input1, input2[i]):
        'func::remove_element_by_index'(input2, i)
        return True
return False
'''