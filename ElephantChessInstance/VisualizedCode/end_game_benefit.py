end_game_benefit = '''
if input0.'xq::pieces'.exist((target.'xq::piece_owner' != input1 and target.'xq::piece_name' == 'xq::Jiang')):
    return 0
return 1
'''