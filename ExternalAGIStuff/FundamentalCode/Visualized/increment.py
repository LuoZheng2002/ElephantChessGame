increment = '''
assert input0 == 'natural_number'
assert input1 == 'natural_number'
reg0 = input0
input0.remove(True)
reg1 = (reg0 + input1)
for i in range(reg1.size):
    input0[i] = reg1[i]
'''