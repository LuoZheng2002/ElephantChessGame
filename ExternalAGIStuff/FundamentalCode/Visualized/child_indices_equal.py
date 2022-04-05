child_indices_equal = '''
if not input0.size === input1.size:
    return False
for i in range(input0.size):
    if input0[i] =!= input1[i]:
        return False
return True
'''