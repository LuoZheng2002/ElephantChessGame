general_strategy = '''
reg0 = 'func::think_from_how_to_win'(input0)
if reg0 != 'Fail':
    return reg0
reg1 = 'func::think_from_operation'(input0)
if reg1 != 'Fail':
    return reg1
return 'Fail'
# 先从赢的角度思考
# 再从能走的行动的角度思考
'''
