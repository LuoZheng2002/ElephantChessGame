operation_func = '''
assert input1 == input0.'xq::whose_turn'
reg0 = input0
reg1 &= reg0.'xq::pieces'
request reg2, reg3, s.t.{'func::batch_logic_and'(reg4)}, provided:
    reg4 = 'list'
    reg4.append(reg2 == 'natural_number')
    reg4.append(reg3 == 'natural_number')
    reg4.append(reg2 >= 0)
    reg4.append(reg2 <= 8)
    reg4.append(reg3 >= 0)
    reg4.append(reg3 <= 9)
    reg4.append(reg1.exist((target.'xq::position'[0] === reg2 and target.'xq::position'[1] === reg3)))
    reg4.append(reg1.find((target.'xq::position'[0] === reg2 and target.'xq::position'[1] === reg3)).'xq::piece_owner' == input1)
reg5 &= reg1.find((target.'xq::position'[0] === reg2 and target.'xq::position'[1] === reg3))
if reg5.'xq::piece_name' == 'xq::Che':
    request reg6, reg7, s.t.{'func::batch_logic_and'(reg8)}, provided:
        reg8 = 'list'
        reg8.append(reg6 == 'natural_number')
        reg8.append(reg7 == 'natural_number')
        reg8.append(reg6 >= 0)
        reg8.append(reg6 <= 8)
        reg8.append(reg7 >= 0)
        reg8.append(reg7 <= 9)
        reg9 = 'list'
        reg9.append(reg6 === reg2)
        reg9.append(reg7 =!= reg3)
        reg9.append(not reg1.exist(((target.'xq::position'[0] === reg2 and target.'xq::position'[1] > 'func::min'(reg7, reg3)) and target.'xq::position'[1] < 'func::max'(reg7, reg3))))
        reg10 = 'func::batch_logic_and'(reg9)
        reg11 = 'list'
        reg11.append(reg7 === reg3)
        reg11.append(reg6 =!= reg2)
        reg11.append(not reg1.exist(((target.'xq::position'[1] === reg3 and target.'xq::position'[0] > 'func::min'(reg6, reg2)) and target.'xq::position'[0] < 'func::max'(reg6, reg2))))
        reg12 = 'func::batch_logic_and'(reg11)
        reg13 = (reg10 or reg12)
        reg8.append(reg13)
        reg8.append(not reg1.exist((target.'xq::piece_owner' == input1 and (target.'xq::position'[0] === reg6 and target.'xq::position'[1] === reg7))))
elif reg5.'xq::piece_name' == 'xq::Ma':
    request reg6, reg7, s.t.{'func::batch_logic_and'(reg8)}, provided:
        reg8 = 'list'
        reg8.append(reg6 == 'natural_number')
        reg8.append(reg7 == 'natural_number')
        reg8.append(reg6 >= 0)
        reg8.append(reg6 <= 8)
        reg8.append(reg7 >= 0)
        reg8.append(reg7 <= 9)
        reg9 = 'list'
        reg9.append(((reg6 === (reg2 + 1) and reg7 === (reg3 + 2)) and not reg1.exist((target.'xq::position'[0] === reg2 and target.'xq::position'[1] === (reg3 + 1)))))
        reg9.append(((reg6 === (reg2 + 2) and reg7 === (reg3 + 1)) and not reg1.exist((target.'xq::position'[0] === (reg2 + 1) and target.'xq::position'[1] === reg3))))
        reg9.append(((reg6 === (reg2 - 1) and reg7 === (reg3 + 2)) and not reg1.exist((target.'xq::position'[0] === reg2 and target.'xq::position'[1] === (reg3 + 1)))))
        reg9.append(((reg6 === (reg2 - 2) and reg7 === (reg3 + 1)) and not reg1.exist((target.'xq::position'[0] === (reg2 - 1) and target.'xq::position'[1] === reg3))))
        reg9.append(((reg6 === (reg2 + 1) and reg7 === (reg3 - 2)) and not reg1.exist((target.'xq::position'[0] === reg2 and target.'xq::position'[1] === (reg3 - 1)))))
        reg9.append(((reg6 === (reg2 + 2) and reg7 === (reg3 - 1)) and not reg1.exist((target.'xq::position'[0] === (reg2 + 1) and target.'xq::position'[1] === reg3))))
        reg9.append(((reg6 === (reg2 - 1) and reg7 === (reg3 - 2)) and not reg1.exist((target.'xq::position'[0] === reg2 and target.'xq::position'[1] === (reg3 - 1)))))
        reg9.append(((reg6 === (reg2 - 2) and reg7 === (reg3 - 1)) and not reg1.exist((target.'xq::position'[0] === (reg2 - 1) and target.'xq::position'[1] === reg3))))
        reg10 = 'func::batch_logic_or'(reg9)
        reg8.append(reg10)
        reg8.append(not reg1.exist((target.'xq::piece_owner' == input1 and (target.'xq::position'[0] === reg6 and target.'xq::position'[1] === reg7))))
elif reg5.'xq::piece_name' == 'xq::Xiang':
    request reg6, reg7, s.t.{'func::batch_logic_and'(reg8)}, provided:
        reg8 = 'list'
        reg8.append(reg6 == 'natural_number')
        reg8.append(reg7 == 'natural_number')
        reg8.append(reg6 >= 0)
        reg8.append(reg6 <= 8)
        if input1 == 'xq::red_team':
            reg8.append(reg7 >= 0)
            reg8.append(reg7 <= 4)
        else:
            reg8.append(reg7 >= 5)
            reg8.append(reg7 <= 9)
        reg9 = 'list'
        reg9.append(((reg6 === (reg2 + 2) and reg7 === (reg3 + 2)) and not reg1.exist((target.'xq::position'[0] === (reg2 + 1) and target.'xq::position'[1] === (reg3 + 1)))))
        reg9.append(((reg6 === (reg2 - 2) and reg7 === (reg3 + 2)) and not reg1.exist((target.'xq::position'[0] === (reg2 - 1) and target.'xq::position'[1] === (reg3 + 1)))))
        reg9.append(((reg6 === (reg2 + 2) and reg7 === (reg3 - 2)) and not reg1.exist((target.'xq::position'[0] === (reg2 + 1) and target.'xq::position'[1] === (reg3 - 1)))))
        reg9.append(((reg6 === (reg2 - 2) and reg7 === (reg3 - 2)) and not reg1.exist((target.'xq::position'[0] === (reg2 - 1) and target.'xq::position'[1] === (reg3 - 1)))))
        reg10 = 'func::batch_logic_or'(reg9)
        reg8.append(reg10)
        reg8.append(not reg1.exist((target.'xq::piece_owner' == input1 and (target.'xq::position'[0] === reg6 and target.'xq::position'[1] === reg7))))
elif reg5.'xq::piece_name' == 'xq::Shi':
    request reg6, reg7, s.t.{'func::batch_logic_and'(reg8)}, provided:
        reg8 = 'list'
        reg8.append(reg6 == 'natural_number')
        reg8.append(reg7 == 'natural_number')
        reg8.append(reg6 >= 3)
        reg8.append(reg6 <= 5)
        if input1 == 'xq::red_team':
            reg8.append(reg7 >= 0)
            reg8.append(reg7 <= 2)
        else:
            reg8.append(reg7 >= 7)
            reg8.append(reg7 <= 9)
        reg9 = 'list'
        reg9.append((reg6 === (reg2 + 1) and reg7 === (reg3 + 1)))
        reg9.append((reg6 === (reg2 - 1) and reg7 === (reg3 + 1)))
        reg9.append((reg6 === (reg2 + 1) and reg7 === (reg3 - 1)))
        reg9.append((reg6 === (reg2 - 1) and reg7 === (reg3 - 1)))
        reg10 = 'func::batch_logic_or'(reg9)
        reg8.append(reg10)
        reg8.append(not reg1.exist((target.'xq::piece_owner' == input1 and (target.'xq::position'[0] === reg6 and target.'xq::position'[1] === reg7))))
elif reg5.'xq::piece_name' == 'xq::Jiang':
    request reg6, reg7, s.t.{'func::batch_logic_and'(reg8)}, provided:
        reg8 = 'list'
        reg8.append(reg6 == 'natural_number')
        reg8.append(reg7 == 'natural_number')
        reg8.append(reg6 >= 3)
        reg8.append(reg6 <= 5)
        if input1 == 'xq::red_team':
            reg8.append(reg7 >= 0)
            reg8.append(reg7 <= 2)
        else:
            reg8.append(reg7 >= 7)
            reg8.append(reg7 <= 9)
        reg9 = 'list'
        reg9.append((reg6 === (reg2 + 1) and reg7 === reg3))
        reg9.append((reg6 === (reg2 - 1) and reg7 === reg3))
        reg9.append((reg6 === reg2 and reg7 === (reg3 + 1)))
        reg9.append((reg6 === reg2 and reg7 === (reg3 - 1)))
        reg10 = 'func::batch_logic_or'(reg9)
        reg8.append(reg10)
        reg8.append(not reg1.exist((target.'xq::piece_owner' == input1 and (target.'xq::position'[0] === reg6 and target.'xq::position'[1] === reg7))))
elif reg5.'xq::piece_name' == 'xq::Pao':
    request reg6, reg7, s.t.{'func::batch_logic_and'(reg8)}, provided:
        reg8 = 'list'
        reg8.append(reg6 == 'natural_number')
        reg8.append(reg7 == 'natural_number')
        reg8.append(reg6 >= 0)
        reg8.append(reg6 <= 8)
        reg8.append(reg7 >= 0)
        reg8.append(reg7 <= 9)
        reg9 = 'list'
        reg9.append(reg6 === reg2)
        reg9.append(reg7 =!= reg3)
        reg9.append(not reg1.exist(((target.'xq::position'[0] === reg2 and target.'xq::position'[1] > 'func::min'(reg7, reg3)) and target.'xq::position'[1] < 'func::max'(reg7, reg3))))
        reg10 = 'func::batch_logic_and'(reg9)
        reg11 = 'list'
        reg11.append(reg7 === reg3)
        reg11.append(reg6 =!= reg2)
        reg11.append(not reg1.exist(((target.'xq::position'[1] === reg3 and target.'xq::position'[0] > 'func::min'(reg6, reg2)) and target.'xq::position'[0] < 'func::max'(reg6, reg2))))
        reg12 = 'func::batch_logic_and'(reg11)
        reg13 = ((reg10 or reg12) and not reg1.exist((target.'xq::position'[0] === reg6 and target.'xq::position'[1] === reg7)))
        reg14 = 'list'
        reg14.append(reg6 === reg2)
        reg14.append(reg7 =!= reg3)
        reg14.append(reg1.count(((target.'xq::position'[0] === reg2 and target.'xq::position'[1] > 'func::min'(reg7, reg3)) and target.'xq::position'[1] < 'func::max'(reg7, reg3))) === 1)
        reg15 = 'func::batch_logic_and'(reg14)
        reg16 = 'list'
        reg16.append(reg7 === reg3)
        reg16.append(reg6 =!= reg2)
        reg16.append(reg1.count(((target.'xq::position'[1] === reg3 and target.'xq::position'[0] > 'func::min'(reg6, reg2)) and target.'xq::position'[0] < 'func::max'(reg6, reg2))) === 1)
        reg17 = 'func::batch_logic_and'(reg16)
        reg18 = ((reg15 or reg17) and reg1.exist((target.'xq::piece_owner' != input1 and (target.'xq::position'[0] === reg6 and target.'xq::position'[1] === reg7))))
        reg19 = (reg13 or reg18)
        reg8.append(reg19)
        reg8.append(not reg1.exist((target.'xq::piece_owner' == input1 and (target.'xq::position'[0] === reg6 and target.'xq::position'[1] === reg7))))
elif reg5.'xq::piece_name' == 'xq::Bing':
    request reg6, reg7, s.t.{'func::batch_logic_and'(reg8)}, provided:
        reg8 = 'list'
        reg8.append(reg6 == 'natural_number')
        reg8.append(reg7 == 'natural_number')
        reg8.append(reg6 >= 0)
        reg8.append(reg6 <= 8)
        reg8.append(reg7 >= 0)
        reg8.append(reg7 <= 9)
        reg9 = 'list'
        if input1 == 'xq::red_team':
            reg10 = (reg6 === reg2 and reg7 === (reg3 + 1))
            reg11 = (reg7 >= 5 and ((reg6 === (reg2 - 1) and reg7 === reg3) or (reg6 === (reg2 + 1) and reg7 === reg3)))
        else:
            reg10 = (reg6 === reg2 and reg7 === (reg3 - 1))
            reg11 = (reg7 <= 4 and ((reg6 === (reg2 - 1) and reg7 === reg3) or (reg6 === (reg2 + 1) and reg7 === reg3)))
        reg12 = (reg10 or reg11)
        reg8.append(reg12)
        reg8.append(not reg1.exist((target.'xq::piece_owner' == input1 and (target.'xq::position'[0] === reg6 and target.'xq::position'[1] === reg7))))
else:
    assert False
if reg1.exist((target.'xq::piece_owner' != input1 and (target.'xq::position'[0] === reg6 and target.'xq::position'[1] === reg7))):
    reg1.remove((target.'xq::piece_owner' != input1 and (target.'xq::position'[0] === reg6 and target.'xq::position'[1] === reg7)))
reg5.'xq::position'[0] = reg6
reg5.'xq::position'[1] = reg7
if input1 == 'xq::red_team':
    reg0.'xq::whose_turn' = 'xq::black_team'
else:
    reg0.'xq::whose_turn' = 'xq::red_team'
return reg0
'''

b = '''
'''
