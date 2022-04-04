end_game_benefit = '''
if input0.'xq::pieces'.exist((target.'xq::piece_owner' != input1 and target.'xq::piece_name' == 'xq::Jiang')):
    return 0
return 1
'''

end_game_benefit_can_be = '''
if 'func'(input0.'x0') + 'func'(input0.'x1') + input0.'x2' == 5:
    return 1
return 0
'''