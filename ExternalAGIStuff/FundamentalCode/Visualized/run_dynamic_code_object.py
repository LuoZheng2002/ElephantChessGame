# input0: code_object
# input1: input_params (input0, input1, ...)
# reg0: regs
# reg1: iterators
# (
run_dynamic_code_object = '''
reg0 = 'dc::runtime_inputs'
for i in range(input1.size):
    reg1<i> = 'dc::input_container'
    reg1<i>.'dc::index' = i
    reg1<i>.'value' = input1[i]
    reg0.append(reg1<i>)
reg2 = 'dc::runtime_registers'
reg3 = 'dc::runtime_iterators'
reg4 = 'dc::runtime_memory'
reg4.'dc::runtime_inputs' &= reg0
reg4.'dc::runtime_registers' &= reg2
reg4.'dc::runtime_iterators' &= reg3
for j in range(input0.size):
    reg5<j> = 'func::process_line'(input0[j], reg4)
    assert reg5<j> != 'dc::line_signal_break'
    if reg5<j> == 'dc::line_signal_return':
        return reg5<j>.'dc::line_return_value'
return 'None'
'''

# input0: expression object, input1: input1, input2: target
solve_expression = '''
if input0 == 'dcr::constexpr':
    return input0.'content'
if input0 == 'dcr::input':
    assert input1.'dc::runtime_inputs'.exist(target.'dc::index' === input0.'dc::index')
    return input1.'dc::runtime_inputs'.find(target.'dc::index' === input0.'dc::index').'value'
if input0 == 'dcr::reg':
    reg0 &= input0.'dc::index'
    reg1 &= 'list'
    for i in range(input0.'dc::child_indices'.size):
        reg1[i] &= 'func::solve_expression'(input0.'dc::child_indices'[i], input1, None)
    assert input1.'dc::runtime_registers'.exist((target.'dc::index' === reg0 and 'func::child_indices_equal'(target.'dc::child_indices', reg1)))
    return input1.'dc::runtime_registers'.find((target.'dc::index' === reg0 and 'func::child_indices_equal'(target.'dc::child_indices', reg1))).'value'
if input0 == 'dcr::iterator':
    assert input1.'dc::runtime_iterators'.exist(target.'dc::index' === input0.'dc::index')
    return input1.'dc::runtime_iterators'.find(target.'dc::index' === input0.'dc::index').'value'
if input0 == 'dcr::call':
    reg0 &= input0.'dc::function_name'
    reg1 &= input0.'dc::function_params'
    reg2 &= 'list'
    for i in range(reg1.size):
        reg2.append('func::solve_expression'(reg1[i], input1, None))
    if 'func::is_code_dynamic'(reg0):
        return 'func::run_dynamic_code_object'('func::get_dynamic_code_object'(reg0), reg2)
    return 'func::run_hardcoded_code'(reg0, reg2)
if input0 == 'dcr::concept_instance':
    return input0.'dc::concept_name'
if input0 == 'dcr::size':
    reg0 &= 'func::solve_expression'(input0.'dc::target_list', input1, None)
    return reg0.size
if (input0 == 'dcr::at' or input0 == 'dcr::at_reverse'):
    reg0 &= 'func::solve_expression'(input0.'dc::target_list', input1, None)
    reg1 &= 'func::solve_expression'(input0.'dc::index', input1, None)
    if input0 == 'dcr::at':
        return reg0[reg1]
    return reg0[!reg1]
if input0 == 'dcr::get_member':
    reg0 &= 'func::solve_expression'(input0.'dc::target_object', input1, None)
    return 'func::get_object_member'(reg0, input0.'dc::member_name')
if input0 == 'dcr::target':
    assert input2 != None
    return input2
if (input0 == 'dcr::find' or input0 == 'dcr::exist'):
    reg0 &= 'func::solve_expression'(input0.'dc::target_list', input1, None)
    for i in range(reg0.size):
        if 'func::solve_expression'(input0.'dc::expression_for_constraint', input1, reg0[i]):
            if input0 == 'dcr::find':
                return reg0[i]
            else:
                return True
    if input0 == 'dcr::find':
        return Fail
    else:
        return False
if input0 == 'dcr::count':
    reg0 &= 'func::solve_expression'(input0.'dc::target_list', input1, None)
    reg1 &= 0
    for i in range(reg0.size):
        if 'func::solve_expression'(input0.'dc::expression_for_constraint', input1, reg0[i]):
            'func::increment'(reg1, 1)
    return reg1
assert False
'''

# input0: line, input1: runtime_memory
process_line = '''
if (input0 == 'dcr::assign' or input0 == 'dcr::assign_as_reference'):
    reg0 &= 'func::solve_expression'(input0.'dc::right_value', input1, None)
    if input0.'dc::left_value' == 'dcr::reg':
        reg1 &= input0.'dc::left_value'.'dc::index'
        reg2 &= 'list'
        for i in range(input0.'dc::left_value'.'dc::child_indices'.size):
            reg2[i] &= 'func::solve_expression'(input0.'dc::left_value'.'dc::child_indices'[i], input1, None)
        assert not input1.'dc::runtime_registers'.exist((target.'dc::index' === reg1 and 'func::child_indices_equal'(target.'dc::child_indices', reg2)))
        reg3 &= 'dc::register_container'
        reg3.'dc::index' &= reg1
        reg3.'dc::child_indices' &= reg2
        if input0 == 'dcr::assign':
            reg3.'value' = reg0
        else:
            reg3.'value' &= reg0 
        input1.'dc::runtime_registers'.append(reg3)
    elif input0.'dc::left_value' == 'dcr::get_member':
        reg1 &= 'func::solve_expression'(input0.'dc::target_object', input1, None)
        'func::set_object_member'(reg1, input0.'dc::member_name', reg0)
    elif (input0.'dc::left_value' == 'dcr::at' or input0.'dc::left_value' == 'dcr::at_reverse'):
        reg1 &= 'func::solve_expression'(input0.'dc::target_list', input1, None)
        reg2 &= 'func::solve_expression'(input0.'dc::index', input1, None)
        if input0.'dc::left_value' == 'dcr::at':
            reg1[reg2] &= reg0
        else:
            reg1[!reg2] &= reg0
    else:
        assert False
    return 'dc::line_signal_normal'
if input0 == 'dcr::return':
    reg0 &= 'dc::line_signal_return'
    reg0.'dc::line_return_value' &= 'func::solve_expression'(input0.'dc::return_value', input1, None)
    return reg0
if input0 == 'dcr::for':
    reg0 &= 'func::solve_expression'(input0.'dc::end_value', input1, None)
    assert not input1.'dc::runtime_iterators'.exist(target.'dc::index' === input0.'dc::iterator_index')
    reg1 &= 'dc::iterator_container'
    reg1.'dc::index' &= input0.'dc::iterator_index'
    reg1.'value' &= 0
    input1.'dc::runtime_iterators'.append(reg1)
    for i in range(reg0):
        for j in range(input0.'dc::for_block'.size):
            reg2<i,j> &= 'func::process_line'(input0.'dc::for_block'[j], input1)
            if reg2<i,j> == 'dc::line_signal_break':
                return 'dc::line_signal_normal'
            elif reg2<i,j> == 'dc::line_signal_return':
                return reg2<i,j>
        reg1.'value' &= (reg1.'value' + 1)
    return 'dc::line_signal_normal'
if input0 == 'dcr::while':
    while 'func::solve_expression'(input0.'dc::expression_for_judging', input1, None):
        for i in range(input0.'dc::while_block'.size):
            reg0<i> &= 'func::process_line'(input0.'dc::while_block'[i], input1)
            if reg0<i> == 'dc::line_signal_break':
                return 'dc::line_signal_normal'
            elif reg0<i> == 'dc::line_signal_return':
                return reg0<i>
    return 'dc::line_signal_normal'
if input0 == 'dcr::break':
    return 'dc::line_signal_break'
if input0 == 'dcr::if':
    if 'func::solve_expression'(input0.'dc::expression_for_judging', input1, None):
        for i in range(input0.'dc::if_block'.size):
            reg0<i> &= 'func::process_line'(input0.'dc::if_block'[i], input1)
            if reg0<i> == 'dc::line_signal_break':
                return 'dc::line_signal_break'
            if reg0<i> == 'dc::line_signal_return':
                return reg0<i>
        return 'dc::line_signal_normal'
    else:
        for i in range(input0.'dc::elif_modules'.size):
            if 'func::solve_expression'(input0.'dc::elif_modules'[i].'dc::expression_for_judging', input1, None):
                reg0<i> &= input0.'dc::elif_modules'[i].'dc::elif_block'
                for j in range(reg0<i>.size):
                    reg1<i,j> &= 'func::process_line'(reg0<i>[j], input1)
                    if reg1<i,j> == 'dc::line_signal_break':
                        return 'dc::line_signal_break'
                    elif reg1<i,j> == 'dc::line_signal_return':
                        return reg1<i.j>
        reg0 &= input0.'dc::else_block'
        for j in range(input0.'dc::else_block'.size):
            reg1<j> &= 'func::process_line'(reg0[j], input1)
            if reg1<j> == 'dc::line_signal_break':
                return 'dc::line_signal_break'
            elif reg1<j> == 'dc::line_signal_return':
                return reg1<j>
        return 'dc::line_signal_normal'
if input0 == 'dcr::assert':
    assert 'func::solve_expression'(input0.'dc::assert_expression', input1, None)
    return 'dc::line_signal_normal'
if input0 == 'dcr::append':
    reg0 &= 'func::solve_expression'(input0.'dc::target_list', input1, None)
    reg1 &= 'func::solve_expression'(input0.'dc::element', input1, None)
    reg0.append(reg1)
    return 'dc::line_signal_normal'
if input0 == 'dcr::remove':
    reg0 &= 'func::solve_expression'(input0.'dc::target_list', input1, None)
    while True:
        reg1 &= 'func::remove_one_element'(input0.'dc::expression_for_constraint', input1, reg0)
        if not reg1:
            break
    return 'dc::line_signal_normal'
if input0 == 'dcr::request':
    assert input0.'dc::requested_registers'.size >= 1
    for i in range(input0.'dc::requested_registers'.size):
        reg0<i> &= input0.'dc::requested_registers'[i]
        assert not input1.'dc::runtime_registers'.exist(target.'dc::index' === reg0<i>)
        reg1<i> &= 'dc::register_container'
        reg1<i>.'dc::index' &= reg0<i>
        reg1<i>.'dc::child_indices' &= 'list'
        reg1<i>.'value' &= 'func::get_input_object'()
        input1.'dc::runtime_registers'.append(reg1<i>)
    reg2 &= input0.'dc::provided_block'
    for j in range(reg2.size):
        reg3<j> &= 'func::process_line'(reg2[j], input1)
        assert reg3<j> == 'dc::line_signal_normal'
    assert 'func::solve_expression'(input0.'dc::expression_for_constraint', input1, None)
    return 'dc::line_signal_normal'
if input0 == 'dcr::call_none_return_func':
    reg0 &= input0.'dc::function_name'
    reg1 &= input0.'dc::function_params'
    reg2 &= 'list'
    for i in range(reg1.size):
        reg2.append('func::solve_expression'(reg1[i], input1, None))
    if 'func::is_code_dynamic'(reg0):
        reg3 &= 'func::run_dynamic_code_object'('func::get_dynamic_code_object'(reg0), reg2)
    else:
        reg3 &= 'func::run_hardcoded_code'(reg0, reg2)
    assert reg3 == None
    return 'dc::line_signal_normal'
assert False
'''