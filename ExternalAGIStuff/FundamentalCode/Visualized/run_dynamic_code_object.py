# input0: code_object
# input1: input_params (input0, input1, ...)
# reg0: regs
# reg1: iterators

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
for i in range(input0.size):
    reg5<i> = 'func::process_line'(input0[i], reg4)
    assert reg5<i> != 'dc::signal_break'
    if reg5<i> == 'dc::signal_return':
        return reg5<i>.'dc::line_return_value'
return 'None'
'''

# input0: expression object
solve_expression = '''
if type(expr) != list or len(expr) == 0:
        raise AGIException('An expression can\'t be of zero size.', special_name='expr', special_str=str(expr))
    # constexpr:
    if len(expr) == 1 and type(expr[0]) != int:
        return expr[0]
    head = expr[0]
    if head == r['input']:
        # format: [input, index_of_input]
        return rsc_mng.input_params[to_integer(expr[1])]
    elif head == r['reg']:
        # format: [reg, index_of_reg, [expr1, expr2, ...]]
        child_index = []
        for i in expr[2]:
            child_index.append(to_integer(solve_expression(i, rsc_mng, target)))
        child_index = tuple(child_index)
        # if to_integer(expr[1]) == 9:
        #     print('reg9:')
        #     print(translate_AGIObject(rsc_mng.get_reg_value(to_integer(expr[1]), child_index)))
        try:
            return rsc_mng.get_reg_value(to_integer(expr[1]), child_index)
        except AGIException as e:
            print(cid_reverse[process_stack[-1].code_id])
            raise e
    elif head == r['iterator']:
        # format: [iterator, index_of_iterator]
        return obj(rsc_mng.get_iterator_value(to_integer(expr[1])))
    elif head == r['call']:
        # format: [call, method_id, [expr1, expr2, ...]]
        code_id = expr[1]
        input_params = []
        for i in expr[2]:
            input_params.append(solve_expression(i, rsc_mng, target))
        result = run_code(code_id, input_params)
        assert type(result) == AGIObject
        return result
    elif head == r['concept_instance']:
        # concept_type, type_id
        type_id = expr[1]
        return create_concept_instance(type_id)
    elif head == r['size']:
        # size, expr
        result = solve_expression(expr[1], rsc_mng, target)
        if type(result) == AGIObject:
            size = get_agi_list(result).size()
        else:
            assert type(result) == AGIList
            size = result.size()
        dout('size', 'Size is ' + str(size))
        return obj(size)
    elif head == r['at'] or head == r['at_reverse']:
        # at/at_reverse, target, index
        target_expr = solve_expression(expr[1], rsc_mng, target)
        index = to_integer(solve_expression(expr[2], rsc_mng, target))
        if type(target_expr) == AGIObject:
            if target_expr.concept_id == cid_of['Fail']:
                return obj('Fail')
            if head == r['at']:
                return get_agi_list(target_expr).get_element(index)
            else:  # head == r['at_reverse']
                return get_agi_list(target_expr).get_element_reverse(index)
        else:
            if type(target_expr) != AGIList:
                raise AGIException('target is supposed to be AGIList or AGIObject',
                                   special_name='type of target', special_str=str(type(target_expr)))
            if head == r['at']:
                return target_expr.get_element(index)
            else:  # head == r['at_reverse']
                return target_expr.get_element_reverse(index)
    elif head == r['get_member']:
        # get_member target member_name
        target_expr = solve_expression(expr[1], rsc_mng, target)
        if target_expr.concept_id == cid_of['Fail']:
            return obj('Fail')
        member_name = expr[2]
        if type(target_expr) == AGIObject:
            return target_expr.attributes[member_name]
        else:
            assert type(target_expr) == dict
            return target_expr[member_name]
    elif head == r['target']:
        if target is None:
            raise AGIException('Target not specified.')
        return target
    elif head == r['find'] or head == r['exist']:
        # find target_expr, constraints_expr
        target_expr = expr[1]
        constraints_expr = expr[2]
        target_obj = solve_expression(target_expr, rsc_mng)
        assert type(target_obj) == AGIObject or AGIList
        if type(target_obj) == AGIObject:
            target_obj = get_agi_list(target_obj)
        for i in range(target_obj.size()):
            constraints_result = solve_expression(constraints_expr, rsc_mng, target_obj.get_element(i))
            if type(constraints_result) != AGIObject or (
                    constraints_result.concept_id != cid_of['True'] and
                    constraints_result.concept_id != cid_of['False'] and
                    constraints_result.concept_id != cid_of['Fail']):
                raise AGIException('Constraints_result should be true or false or fail.')
            if constraints_result.concept_id == cid_of['True']:
                if head == r['find']:
                    return target_obj.get_element(i)
                else:
                    return obj(True)
        if head == r['find']:
            dout('warning', 'Warning: A find process failed!')
            return obj('Fail')
        else:
            return obj(False)
    elif head == r['count']:
        # count target_expr, constraints_expr
        target_expr = expr[1]
        constraints_expr = expr[2]
        target_obj = solve_expression(target_expr, rsc_mng)
        assert type(target_obj) == AGIObject or AGIList
        if type(target_obj) == AGIObject:
            target_obj = get_agi_list(target_obj)
        count = 0
        for i in range(target_obj.size()):
            constraints_result = solve_expression(constraints_expr, rsc_mng, target_obj.get_element(i))
            if type(constraints_result) != AGIObject or (
                    constraints_result.concept_id != cid_of['True'] and
                    constraints_result.concept_id != cid_of['False'] and
                    constraints_result.concept_id != cid_of['Fail']):
                raise AGIException('Constraints_result should be true or false or fail.')
            if constraints_result.concept_id == cid_of['True']:
                count += 1
        return obj(count)
    else:
        raise AGIException('Unexpected word at the beginning of an expression.')
'''

# input0: line, input1: runtime_memory
process_line = '''
if (input0 == 'dcr::assign' or input0 == 'dcr::assign_as_reference'):
    reg0 &= 'func::solve_expression'(input0.'dc::right_value')
    if input0.'dc::left_value' == 'dcr::reg':
        reg1 &= 'func::solve_expression'(input0.'dc::left_value'.'dc::index')
        reg2 &= 'list'
        for i in range(input0.'dc::left_value'.'dc::child_indices'.size):
            reg2[i] &= 'func::solve_expression'(input0.'dc::left_value'.'dc::child_indices'[i])
        assert not input1.'dc::runtime_registers'.exist((target.'dc::index' == reg1 and target.'dc::child_indices' == reg2)):
        reg3 &= 'dc::runtime_register'
        reg3.'dc::index' &= reg1
        reg3.'dc::child_indices' &= reg2
        if input0 == 'dcr::assign':
            reg3.'value' = reg0
        else:
            reg3.'value' &= reg0 
        input1.'dc::runtime_registers'.append(reg3)
    elif input0.'dc::left_value' == 'dcr::get_member':
        reg1 &= 'func::solve_expression'(input0.'dc::target_object')
        reg2 &= input0.'dc::member_name'
        'func::set_object_member'(reg1, reg2, reg0)
    elif (input0.'dc::left_value' == 'dcr::at' or input0.'dc::left_value' == 'dcr::at_reverse'):
        reg1 &= 'func::solve_expression'(input0.'dc::target_list')
        reg2 &= 'func::solve_expression'(input0.'dc::index')
        if input0.'dc::left_value' == 'dcr::at':
            reg1[reg2] &= reg0
        else:
            reg1[!reg2] &= reg0
    return 'dc::line_signal_normal'
elif input0 == 'dcr::return':
    reg1 &= 'dc::line_signal_return'
    reg1.'dc::line_return_value' &= 'func::solve_expression'(input0.'dc::return_value')
elif input0 == 'dcr::for':
    input0.'dc::iterator_index'
    reg1 &= 'func::solve_expression'(input0.'dc::end_value')
    assert not input1.'runtime_iterators'.exist(target.'dc::index' == input0.'dc::iterator_index')
    reg2 &= 'dc::iterator_container'
    reg2.'dc::index' &= input0.'dc::iterator_index'
    reg2.'value' &= 0
    
    
    is_break = False
    while rsc_mng.get_iterator_value(iter_id) < end_value:
        dout('for_loop_hint', 'for looped!')
        for for_line in for_lines:
            return_value_in_for = process_line(for_line, rsc_mng, scope_in_for)
            if return_value_in_for['value_type'] == 'return':
                return_value = return_value_in_for
                is_break = True
                break
            elif return_value_in_for['value_type'] == 'break':
                is_break = True
                break
        if is_break:
            break
        dout('iterator_value', 'Iterator value now is:' + str(rsc_mng.get_iterator_value(iter_id)))
        rsc_mng.update_iterator(iter_id)
elif head == r['while']:
    # format: [while, statement, [line1, line2, line3, ...]]
    statement = line[1]
    while_lines = line[2]
    is_break = False
    while True:
        result = solve_expression(statement, rsc_mng)
        assert type(result) == bool
        if not result:
            break
        for while_line in while_lines:
            return_value_in_while = process_line(while_line, rsc_mng, scope_info)
            if return_value_in_while['value_type'] == 'return':
                return_value = return_value_in_while
                is_break = True
                break
            elif return_value_in_while['value_type'] == 'break':
                is_break = True
                break
        if is_break:
            break
elif head == r['break']:
    return_value = {'value_type': 'break', 'value': None}
elif head == r['if']:
    # format: [if, statement, [line1, line2, ...], [else_if_block1, else_if_block2, ...], else_lines]
    # else_if_blocks: [statement, [line1, line2, ...]]
    # else_block: [line1, line2, ...]
    if_statement = line[1]
    if_lines = line[2]
    else_if_blocks = line[3]
    else_lines = line[4]

    # process if statement
    result = solve_expression(if_statement, rsc_mng)
    if result.concept_id == cid_of['True']:
        dout('if', 'if succeeded')
        for if_line in if_lines:
            if_return_value = process_line(if_line, rsc_mng, scope_info)
            if if_return_value['value_type'] == 'break':
                return_value = {'value_type': 'break', 'value': None}
                break
            elif if_return_value['value_type'] == 'return':
                return_value = if_return_value
                break
    else:  # if "if" statement fails, else if and else statements have an opportunity to be executed
        dout('if', 'if failed')
        executed = False
        for else_if_block in else_if_blocks:
            else_if_statement = else_if_block[0]
            else_if_lines = else_if_block[1]
            result = solve_expression(else_if_statement, rsc_mng)
            if result.concept_id == cid_of['True']:
                dout('if', 'elif succeeded')
                executed = True
                # execute the else_if lines
                for else_if_line in else_if_lines:
                    elif_return_value = process_line(else_if_line, rsc_mng, scope_info)
                    if elif_return_value['value_type'] == 'break':
                        return_value = {'value_type': 'break', 'value': None}
                        break
                    elif elif_return_value['value_type'] == 'return':
                        return_value = elif_return_value
                        break
                # this else_if block is executed, meaning that other else_if block should not be executed
                break
            else:
                dout('if', 'elif failed')
        # execute else block
        if not executed:
            for else_line in else_lines:
                else_return_value = process_line(else_line, rsc_mng, scope_info)
                if else_return_value['value_type'] == 'break':
                    return_value = {'value_type': 'break', 'value': None}
                    break
                elif else_return_value['value_type'] == 'return':
                    return_value = else_return_value
                    break
elif head == r['assert']:
    target_expr = line[1]
    if solve_expression(target_expr, rsc_mng).concept_id == cid_of['False']:
        raise AGIException('Assertion Failed in Dynamic Code!')
elif head == r['append']:
    # append, array, element
    target_expr = solve_expression(line[1], rsc_mng)
    element = deepcopy(solve_expression(line[2], rsc_mng))
    if type(target_expr) == AGIList:
        target_expr.append(element)
    elif type(target_expr) == AGIObject:
        get_agi_list(target_expr).append(element)
elif head == r['remove']:
    # remove, array, expr
    target_expr = solve_expression(line[1], rsc_mng)
    constraints_expr = line[2]
    assert type(target_expr) == AGIObject or type(target_expr) == AGIList
    if type(target_expr) == AGIObject:
        target_expr = get_agi_list(target_expr)
    go_on = True
    while go_on:
        found = False
        for i in range(target_expr.size()):
            result = solve_expression(constraints_expr, rsc_mng, target_expr.get_element(i))
            if type(result) != AGIObject or (
                    result.concept_id != cid_of['True'] and result.concept_id != cid_of['False']):
                raise AGIException('The result should be true or false.')
            if result.concept_id == cid_of['True']:
                target_expr.remove(i)
                found = True
                break
        if not found:
            go_on = False
elif head == r['request']:
    # request [obj(1), obj(2)], constraints_expr lines
    registers = line[1]
    constraints_expr = line[2]
    provided_lines = line[3]
    for register in registers:
        reg_id = to_integer(register)
        if not rsc_mng.has_reg(reg_id, tuple()):
            rsc_mng.create_reg(reg_id, tuple(), tuple())
        str_input = input('The freaking dynamic code asks you to fill in reg' + str(reg_id) + '!\n')
        input_obj = translate_input(str_input)
        rsc_mng.set_reg_value(reg_id, tuple(), input_obj)
    for provided_line in provided_lines:
        return_value = process_line(provided_line, rsc_mng, scope_info)
        assert return_value['value_type'] is None and return_value['value'] is None
    constraints_test = solve_expression(constraints_expr, rsc_mng)
    if type(constraints_test) != AGIObject or (
            constraints_test.concept_id != cid_of['True'] and constraints_test.concept_id != cid_of['False']):
        raise AGIException('Constraints test result should be true or false.')
    if constraints_test.concept_id == cid_of['False']:
        raise AGIException('Your inputs don\'t satisfy the constraints!', trace_back=False)
else:
    raise AGIException('Unexpected word at the beginning of a line.')
return return_value
'''