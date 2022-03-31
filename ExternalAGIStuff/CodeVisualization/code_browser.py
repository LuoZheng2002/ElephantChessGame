from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from exception import AGIException

number_to_letter = {0: 'i', 1: 'j', 2: 'k', 3: 'l', 4: 'm', 5: 'n', 6: 'o', 7: 'p', 8: 'q', 9: 'r',
                    10: 's', 11: 't', 12: 'u', 13: 'v', 14: 'w', 15: 'x', 16: 'y', 17: 'z'}
letter_to_number = dict([(i, j) for (j, i) in number_to_letter.items()])


def iter_to_str(iter_id: int) -> str:
    if iter_id in number_to_letter.keys():
        return number_to_letter[iter_id]
    return 'iter' + str(iter_id)


def expr_to_str(expr: list) -> str:
    if len(expr) == 1 and type(expr[0]) != int:
        if type(expr[0]) == AGIObject:
            return to_str(expr[0])
        return '[Strange stuff]'
    head = expr[0]
    if head == r['input']:
        input_id = to_integer(expr[1])
        return 'input' + str(input_id)
    elif head == r['reg']:
        reg_id = to_integer(expr[1])
        child_indices = expr[2]
        expr_result = 'reg' + str(reg_id)
        if child_indices:
            expr_result += '<'
            for index in child_indices:
                index_expr = expr_to_str(index)
                expr_result += index_expr + ','
            expr_result = expr_result[:-1]
            expr_result += '>'
        return expr_result
    elif head == r['iterator']:
        iter_id = to_integer(expr[1])
        return iter_to_str(iter_id)
    elif head == r['call']:
        code_id = expr[1]
        params = expr[2]
        if code_id == cid_of['func::sum']:
            param1 = expr_to_str(params[0])
            param2 = expr_to_str(params[1])
            return '(' + param1 + ' + ' + param2 + ')'
        elif code_id == cid_of['func::compare_concepts']:
            param1 = expr_to_str(params[0])
            param2 = expr_to_str(params[1])
            return param1 + ' == ' + param2
        elif code_id == cid_of['func::math_equal']:
            param1 = expr_to_str(params[0])
            param2 = expr_to_str(params[1])
            return param1 + ' === ' + param2
        elif code_id == cid_of['func::logic_and']:
            param1 = expr_to_str(params[0])
            param2 = expr_to_str(params[1])
            return '(' + param1 + ' and ' + param2 + ')'
        elif code_id == cid_of['func::logic_or']:
            param1 = expr_to_str(params[0])
            param2 = expr_to_str(params[1])
            return '(' + param1 + ' or ' + param2 + ')'
        elif code_id == cid_of['func::logic_not']:
            param = expr_to_str(params[0])
            return 'not ' + param
        elif code_id == cid_of['func::greater_than']:
            param1 = expr_to_str(params[0])
            param2 = expr_to_str(params[1])
            return param1 + ' > ' + param2
        elif code_id == cid_of['func::less_than']:
            param1 = expr_to_str(params[0])
            param2 = expr_to_str(params[1])
            return param1 + ' < ' + param2
        elif code_id == cid_of['func::greater_than_or_equal_to']:
            param1 = expr_to_str(params[0])
            param2 = expr_to_str(params[1])
            return param1 + ' >= ' + param2
        elif code_id == cid_of['func::less_than_or_equal_to']:
            param1 = expr_to_str(params[0])
            param2 = expr_to_str(params[1])
            return param1 + ' <= ' + param2
        else:
            expr_result = cid_reverse[code_id] + '('
            for param in params:
                param_expr = expr_to_str(param)
                expr_result += param_expr + ', '
            if params:
                expr_result = expr_result[: -2]
            expr_result += ')'
            return expr_result
    elif head == r['concept_instance']:
        concept_id = expr[1]
        return '\'' + cid_reverse[concept_id] + '\''
    elif head == r['size']:
        target_expr = expr_to_str(expr[1])
        return target_expr + '.size'
    elif head == r['get_member']:
        target_expr = expr_to_str(expr[1])
        member_name = expr[2]
        return target_expr + '.\'' + cid_reverse[member_name] + '\''
    elif head == r['at']:
        target_expr = expr_to_str(expr[1])
        index = expr_to_str(expr[2])
        return target_expr + '[' + index + ']'
    elif head == r['at_reverse']:
        target_expr = expr_to_str(expr[1])
        index = expr_to_str(expr[2])
        return target_expr + '[!' + index + ']'
    elif head == r['find']:
        target_expr = expr_to_str(expr[1])
        constraints_expr = expr_to_str(expr[2])
        return target_expr + '.find(' + constraints_expr + ')'
    elif head == r['exist']:
        target_expr = expr_to_str(expr[1])
        constraints_expr = expr_to_str(expr[2])
        return target_expr + '.exist(' + constraints_expr + ')'
    elif head == r['target']:
        return 'target'
    else:
        raise AGIException('Unexpected head of expression.')


def add_indentation(line_str, indentation_count) -> str:
    result = str()
    for i in range(indentation_count):
        result += '    '
    result += line_str
    return result


def visualize_code(code: list, indentation_count=0) -> list:
    result = list()
    for line in code:
        head = line[0]
        if head == r['assign']:
            expr_str1 = expr_to_str(line[1])
            expr_str2 = expr_to_str(line[2])
            line_str = expr_str1 + ' = ' + expr_str2
            result.append(add_indentation(line_str, indentation_count))
        elif head == r['assign_as_reference']:
            expr_str1 = expr_to_str(line[1])
            expr_str2 = expr_to_str(line[2])
            line_str = expr_str1 + ' &= ' + expr_str2
            result.append(add_indentation(line_str, indentation_count))
        elif head == r['return']:
            expr_str = expr_to_str(line[1])
            line_str = 'return ' + expr_str
            result.append(add_indentation(line_str, indentation_count))
        elif head == r['assert']:
            expr_str = expr_to_str(line[1])
            line_str = 'assert ' + expr_str
            result.append(add_indentation(line_str, indentation_count))
        elif head == r['for']:
            iter_id = to_integer(line[1])
            end_value = expr_to_str(line[2])
            for_lines = line[3]
            line_str = 'for ' + iter_to_str(iter_id) + ' in range(' + end_value + '):'
            result.append(add_indentation(line_str, indentation_count))
            result += visualize_code(for_lines, indentation_count + 1)
        elif head == r['while']:
            judging_expr = expr_to_str(line[1])
            while_lines = line[2]
            line_str = 'while ' + judging_expr + ':'
            result.append(add_indentation(line_str, indentation_count))
            result += visualize_code(while_lines, indentation_count + 1)
        elif head == r['break']:
            line_str = 'break'
            result.append(add_indentation(line_str, indentation_count))
        elif head == r['if']:
            judging_expr = expr_to_str(line[1])
            if_lines = line[2]
            elif_blocks = line[3]
            else_lines = line[4]
            line_str = 'if ' + judging_expr + ':'
            result.append(add_indentation(line_str, indentation_count))
            result += visualize_code(if_lines, indentation_count + 1)
            for elif_block in elif_blocks:
                elif_judging_expr = expr_to_str(elif_block[0])
                elif_lines = elif_block[1]
                elif_line_str = 'elif ' + elif_judging_expr + ':'
                result.append(add_indentation(elif_line_str, indentation_count))
                result += visualize_code(elif_lines, indentation_count + 1)
            if else_lines:
                result.append(add_indentation('else:', indentation_count))
                result += visualize_code(else_lines, indentation_count + 1)
        elif head == r['append']:
            target_expr = expr_to_str(line[1])
            element = expr_to_str(line[2])
            line_str = target_expr + '.append(' + element + ')'
            result.append(add_indentation(line_str, indentation_count))
        elif head == r['remove']:
            target_expr = expr_to_str(line[1])
            element = expr_to_str(line[2])
            line_str = target_expr + '.remove(' + element + ')'
            result.append(add_indentation(line_str, indentation_count))
        elif head == r['request']:
            array_of_reg_ids = line[1]
            constraints_expr = expr_to_str(line[2])
            provided_lines = line[3]
            line_str = 'request '
            assert array_of_reg_ids
            for reg_id in array_of_reg_ids:
                line_str += 'reg' + str(to_integer(reg_id)) + ', '
            line_str += 's.t.{' + constraints_expr + '}, provided:'
            result.append(add_indentation(line_str, indentation_count))
            result += visualize_code(provided_lines, indentation_count + 1)
        else:
            raise AGIException('Unexpected head of line.')
    return result

