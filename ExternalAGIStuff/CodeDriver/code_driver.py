from exception import AGIException
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject, AGIList, get_agi_list
from copy import deepcopy
from ExternalAGIStuff.CodeDriver.runtime_memory import ResourceManager
from ExternalAGIStuff.IDs.reserved_keywords import r, rr
from ExternalAGIStuff.CodeDriver.concept_instance_creator import create_concept_instance
from ExternalAGIStuff.CodeDriver.code_getter import get_code
from ExternalAGIStuff.HardcodedFunctions.hardcoded_function_ids import hardcoded_function_linker
from ExternalAGIStuff.IDs.to_object import obj, to_integer, to_str, translate_input
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeVisualization.code_browser import visualize_line
from debug import dout, debug_on, debug_on_all
from ExternalAGIStuff.HardcodedFunctions.run_hardcoded_code import run_hardcoded_code
from ExternalAGIStuff.HardcodedFunctions.is_code_dynamic import is_code_dynamic
from ExternalAGIStuff.CodeVisualization.StructureVisualization.translate_AGIObject import translate_AGIObject
from ExternalAGIStuff.CodeDriver.process_stack import process_stack


class Process:
    next_stack_count = 0

    def __init__(self, code_id: int, input_params: list):
        self.code_id = code_id
        self.input_params = input_params
        self.stack_count = Process.next_stack_count
        Process.next_stack_count += 1

    def __del__(self):
        Process.next_stack_count -= 1


class CodeIterator:
    def __init__(self, method_code):
        self.list_codes = method_code
        self.line_count = len(method_code)
        self.current_line = None
        self.next_line_index = 0  # line is also counted from 0

    def get_next_line(self):
        self.current_line = self.list_codes[self.next_line_index]
        self.next_line_index += 1

    def end_of_code(self) -> bool:
        return self.next_line_index >= self.line_count


def solve_expression(expr: list,
                     rsc_mng: ResourceManager,
                     target=None) -> AGIObject or AGIList:
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
        child_indices = []
        for i in expr[2]:
            child_indices.append(to_integer(solve_expression(i, rsc_mng, target)))
        child_indices = tuple(child_indices)
        # if to_integer(expr[1]) == 9:
        #     print('reg9:')
        #     print(translate_AGIObject(rsc_mng.get_reg_value(to_integer(expr[1]), child_index)))
        try:
            return rsc_mng.get_reg_value(to_integer(expr[1]), child_indices)
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
            if type(result) != AGIList:
                print(type(result))
                assert False
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
            if member_name not in target_expr.attributes.keys():
                print(cid_reverse[target_expr.concept_id])
                print(cid_reverse[member_name])
                assert False
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


def process_line(line, rsc_mng: ResourceManager) -> dict:
    # return value: {value_type:None/'break'/'return', value:None/None/[return value]}
    global process_stack
    if debug_on_all and debug_on['line'] and len(process_stack) == 2:
        visualized = visualize_line(line)
        for i in visualized:
            print(i)
    return_value = {'value_type': None, 'value': None}
    head = line[0]
    # print(rr[head])
    # print(line)
    if head == r['assign'] or head == r['assign_as_reference']:  # format: [assign, expr, expr]
        lhs_expr = line[1]
        rhs_expr = line[2]
        # because taking an element from a container and modifying it
        # doesn't really modify the element in the container
        # e.g. b = a[1]; b = 1 doesn't make a[1] to be 1
        # so we need to trace the container and the position of the element in the container
        # so that we can do something like a[1] = 2 to modify a[1]
        # lhs = [element's container, at/at_reverse/get_member, index or member name]
        lhs = [None, None, None]
        head_of_lhs = lhs_expr[0]
        reg_index = None  # only for head_of_lhs == r['reg']
        child_indices = None  # only for head_of_lhs == r['reg']
        if head_of_lhs == r['reg']:  # format: [reg, index of reg, [expr1, expr2, ...]]
            # modifying register itself, so no need for the tricks above
            reg_index = to_integer(lhs_expr[1])
            child_expressions = lhs_expr[2]
            # get child_index
            child_indices = []
            for expr in child_expressions:
                child_indices.append(to_integer(solve_expression(expr, rsc_mng)))
            child_indices = tuple(child_indices)
            # assert target register hasn't been created
            # because normally we don't want an existing register to be rewritten
            if not rsc_mng.has_reg(reg_index, child_indices):
                rsc_mng.create_reg(reg_index, child_indices)
        elif head_of_lhs == r['at'] or head_of_lhs == r['at_reverse']:
            # at, [expr], [expr]
            target_expr = solve_expression(lhs_expr[1], rsc_mng)
            if type(target_expr) == AGIObject:
                lhs[0] = get_agi_list(target_expr)
            else:
                assert type(target_expr) == AGIList
                lhs[0] = target_expr
            lhs[1] = head_of_lhs  # 'at' or 'at_reverse'
            lhs[2] = to_integer(solve_expression(lhs_expr[2], rsc_mng))
        elif head_of_lhs == r['get_member']:
            # get_member, [expr], constexpr
            target_expr = solve_expression(lhs_expr[1], rsc_mng)
            if type(target_expr) == AGIObject:
                lhs[0] = target_expr.attributes
            else:
                assert type(target_expr) == dict
                lhs[0] = target_expr
            lhs[1] = head_of_lhs
            lhs[2] = lhs_expr[2]
        else:
            raise AGIException(20)
        # solve for rhs:
        rhs = solve_expression(rhs_expr, rsc_mng)
        # assign rhs to lhs:
        if lhs[1] is None:  # lhs[2] is None too, means that lhs[0] is register object
            if head == r['assign']:
                rsc_mng.set_reg_value(reg_index, child_indices, deepcopy(rhs))
            else:
                rsc_mng.set_reg_value(reg_index, child_indices, rhs)
            debug_string = 'reg' + str(reg_index)
            if child_indices:
                debug_string += '<'
                for i in child_indices:
                    debug_string += str(i) + ','
                debug_string = debug_string[: len(debug_string) - 1]
                debug_string += '>'
            if type(rhs) == AGIObject:
                debug_string += '\'s value is set to \'' + to_str(rhs) + '\''
            else:
                debug_string += '\'s value is set to \'an AGIList\''
            dout('register', debug_string)
        else:
            # if lhs[1] == r['at'] or lhs[1] == r['at_reverse'], then lhs[0] must be an AGIList
            # because lhs[0] is the product of calling get_agi_list when target is an AGIObject
            if lhs[1] == r['at']:
                if head == r['assign']:
                    lhs[0].set_forward(lhs[2], deepcopy(rhs))
                else:
                    lhs[0].set_forward(lhs[2], rhs)
            elif lhs[1] == r['at_reverse']:
                if head == r['assign']:
                    lhs[0].set_reverse(lhs[2], deepcopy(rhs))
                else:
                    lhs[0].set_reverse(lhs[2], rhs)
            else:  # lhs[1] == r['get_member']
                if type(lhs[0]) != AGIObject and type(lhs[0]) != dict:
                    raise AGIException('Can only call "get_member" towards an AGIObject or a dict.')
                if head == r['assign']:
                    lhs[0][lhs[2]] = deepcopy(rhs)
                else:
                    lhs[0][lhs[2]] = rhs
    elif head == r['return']:
        result = solve_expression(line[1], rsc_mng)
        return_value = {'value_type': 'return', 'value': result}
    elif head == r['for']:
        # for, iter_id, end_value, [line1, line2, ...]
        iter_id = to_integer(line[1])
        end_value = to_integer(solve_expression(line[2], rsc_mng))
        dout('for_end_value', 'end value is' + str(end_value))
        for_lines = line[3]
        if not rsc_mng.has_iterator(iter_id):
            rsc_mng.create_iterator(iter_id)
        else:
            rsc_mng.zero_iterator(iter_id)
            print('iterator' + str(iter_id) + ' zeroed!')
        is_break = False
        while rsc_mng.get_iterator_value(iter_id) < end_value:
            loop_count = 0
            dout('for_loop_hint', 'for looped!')
            if process_stack[-1].stack_count == 0:
                dout('iterator_value',
                     'Iterator' + str(iter_id) + '\'s value now is:' + str(rsc_mng.get_iterator_value(iter_id)))

            for for_line in for_lines:
                return_value_in_for = process_line(for_line, rsc_mng)
                if return_value_in_for['value_type'] == 'return':
                    return_value = return_value_in_for
                    is_break = True
                    break
                elif return_value_in_for['value_type'] == 'break':
                    is_break = True
                    break
            if is_break:
                break
            rsc_mng.update_iterator(iter_id)
            # print('iterator' + str(iter_id) + ' updated!')
            loop_count += 1
            if loop_count == 100:
                raise AGIException('While loop does not stop.')
    elif head == r['while']:
        # format: [while, statement, [line1, line2, line3, ...]]
        statement = line[1]
        while_lines = line[2]
        is_break = False
        while True:
            loop_count = 0
            result = solve_expression(statement, rsc_mng)
            assert type(result) == AGIObject
            if result.concept_id == cid_of['False'] or result.concept_id == cid_of['Fail']:
                break
            for while_line in while_lines:
                return_value_in_while = process_line(while_line, rsc_mng)
                if return_value_in_while['value_type'] == 'return':
                    return_value = return_value_in_while
                    is_break = True
                    break
                elif return_value_in_while['value_type'] == 'break':
                    is_break = True
                    break
            if is_break:
                break
            loop_count += 1
            if loop_count == 100:
                raise AGIException('While loop does not stop.')
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
                if_return_value = process_line(if_line, rsc_mng)
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
                        elif_return_value = process_line(else_if_line, rsc_mng)
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
                    else_return_value = process_line(else_line, rsc_mng)
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
        element = solve_expression(line[2], rsc_mng)
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
            loop_count = 0
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
            loop_count += 1
            if loop_count == 100:
                raise AGIException('While loop does not stop.')
    elif head == r['request']:
        # request [obj(1), obj(2)], constraints_expr lines
        registers = line[1]
        constraints_expr = line[2]
        provided_lines = line[3]
        for register in registers:
            reg_index = to_integer(register)
            if not rsc_mng.has_reg(reg_index, tuple()):
                rsc_mng.create_reg(reg_index, tuple())
            str_input = input('The freaking dynamic code asks you to fill in reg' + str(reg_index) + '!\n')
            input_obj = translate_input(str_input)
            rsc_mng.set_reg_value(reg_index, tuple(), input_obj)
        for provided_line in provided_lines:
            return_value = process_line(provided_line, rsc_mng)
            assert return_value['value_type'] is None and return_value['value'] is None
        constraints_test = solve_expression(constraints_expr, rsc_mng)
        if type(constraints_test) != AGIObject or (
                constraints_test.concept_id != cid_of['True'] and constraints_test.concept_id != cid_of['False']):
            raise AGIException('Constraints test result should be true or false.')
        if constraints_test.concept_id == cid_of['False']:
            raise AGIException('Your inputs don\'t satisfy the constraints!', trace_back=False)
    elif head == r['call_none_return_func']:
        # format: [call, method_id, [expr1, expr2, ...]]
        code_id = line[1]
        input_params = []
        for i in line[2]:
            input_params.append(solve_expression(i, rsc_mng))
        result = run_code(code_id, input_params)
        assert result is None
    else:
        raise AGIException('Unexpected word at the beginning of a line.')
    return return_value


def run_code(code_id, input_params: list, code=None) -> AGIObject or None:
    if code_id in hardcoded_function_linker.keys():
        try:
            return hardcoded_function_linker[code_id](input_params)
        except AGIException as e:
            print([cid_reverse[i.concept_id] for i in input_params])
            raise e
    if code_id == cid_of['func::run_hardcoded_code']:
        return run_hardcoded_code(input_params)
    if code_id == cid_of['func::is_code_dynamic']:
        return is_code_dynamic(input_params)
    # local resource manager creation
    global process_stack
    process_stack.append(Process(code_id, input_params))
    if code_id is not None:
        debug_string = '\nEnter process (stack count = ' + str(process_stack[-1].stack_count) + '): ' + '\'' + \
                       cid_reverse[
                           code_id] + '\'!\n' + 'Input params are:\n'
    else:
        debug_string = '\nEnter process (stack count = ' + str(process_stack[-1].stack_count) + '): ' + '\'' + \
                       'Unknown' + '\'!\n' + 'Input params are:\n'
    for param in input_params:
        if type(param) == AGIList:
            debug_string += "'AGIList'"
        else:
            debug_string += '\'' + to_str(param) + '\' '
    dout('process', debug_string)
    rsc_mng = ResourceManager(input_params)
    if code is None:
        method_code = get_code(code_id)
    else:
        method_code = code
    # CodeIterator creation
    ci = CodeIterator(method_code)
    # start processing
    while not ci.end_of_code():
        loop_count = 0
        ci.get_next_line()
        line_return_value = process_line(ci.current_line, rsc_mng)
        if line_return_value['value_type'] == 'return':
            if code_id is not None:
                dout('process',
                     'Exit process (stack count = ' + str(process_stack[-1].stack_count) + '): \'' + cid_reverse[
                         process_stack[-1].code_id] + '\'!')
            else:
                dout('process',
                     'Exit process (stack count = ' + str(process_stack[-1].stack_count) + '): \'' + 'Unknown' + '\'!')
            dout('return', 'Return value is: \'' + to_str(line_return_value['value']) + '\'!\n')
            process_stack.pop()
            return line_return_value['value']
        elif line_return_value['value_type'] == 'break':
            raise AGIException('Try to break without being in a for or while loop.')
        else:
            if line_return_value['value_type'] is not None:
                raise AGIException('Unexpected value type for a return value of a line.')
        loop_count += 1
        if loop_count == 100:
            raise AGIException('While loop does not stop.')
    if code_id is not None:
        dout('process',
             'Exit process without return (stack count = ' + str(process_stack[-1].stack_count) + '): \'' + cid_reverse[
                 process_stack[-1].code_id] + '\'!')
    else:
        dout('process',
             'Exit process without return (stack count = ' + str(
                 process_stack[-1].stack_count) + '): \'' + 'Unknown' + '\'!')
    process_stack.pop()
    return
