end_game_func = '''
reg0 = input0.'xq::pieces'
if reg0.count(target.'xq::piece_name' == 'xq::Jiang') === 2:
    return False
else:
    return True
'''