from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException


def rightest_naked_dot(string_code: str) -> int:
    string_code_copy = string_code
    rightest_naked = -1
    while string_code_copy.find('.', rightest_naked + 1) != -1:
        position = string_code_copy.find('.', rightest_naked + 1)
        bracket_count = 0
        for i in range(position):
            if string_code_copy[i] == '(':
                bracket_count += 1
            elif string_code_copy[i] == ')':
                bracket_count -= 1
        if bracket_count == 0:
            rightest_naked = position
        string_code_copy = string_code_copy.replace('.', '@', 1)
    return rightest_naked


def slice_code(string_code: str) -> list:
    result = list()
    string_code_copy = string_code
    if string_code_copy[0] == '\n':
        string_code_copy = string_code_copy[1:]
    while string_code_copy.find('\n') != -1:
        return_pos = string_code_copy.find('\n')
        result.append(string_code_copy[:return_pos])
        string_code_copy = string_code_copy[return_pos + 1:]
    if string_code_copy != '':
        result.append(string_code_copy)
    return result


def find_middle(target_str: str, sub_str: str, target_bracket=1) -> int:
    target_str_copy = target_str
    while target_str_copy.find(sub_str) != -1:
        pos = target_str_copy.find(sub_str)
        bracket_count = 0
        for i in range(pos):
            if target_str_copy[i] == '(':
                bracket_count += 1
            elif target_str_copy[i] == ')':
                bracket_count -= 1
        if not bracket_count >= target_bracket:
            print(target_str)
            assert False
        if bracket_count > target_bracket:
            target_list_copy = list(target_str_copy)
            for j in range(len(sub_str)):
                target_list_copy[pos + j] = '@'
            target_str_copy = str()
            for j in target_list_copy:
                target_str_copy += j
        else:
            return pos
    return -1


def generate_expression(string_expr: str) -> str:
    if string_expr[0] == '(' and string_expr[-1] == ')':
        func_name = None
        if find_middle(string_expr, ' + ') != -1:
            middle_pos = find_middle(string_expr, ' + ')
            func_name = 'func::sum'
            # print('whole: ' + string_expr)
            # print('left: ' + string_expr[1: middle_pos])
            # print('right: ' + string_expr[middle_pos + 3: -1])
            left_expr = generate_expression(string_expr[1: middle_pos])
            right_expr = generate_expression(string_expr[middle_pos + 3: -1])
        elif find_middle(string_expr, ' - ') != -1:
            middle_pos = find_middle(string_expr, ' - ')
            func_name = 'func::difference'
            left_expr = generate_expression(string_expr[1: middle_pos])
            right_expr = generate_expression(string_expr[middle_pos + 3: -1])
        elif find_middle(string_expr, ' and ') != -1:
            middle_pos = find_middle(string_expr, ' and ')
            func_name = 'func::logic_and'
            left_expr = generate_expression(string_expr[1: middle_pos])
            right_expr = generate_expression(string_expr[middle_pos + 5: -1])
        elif find_middle(string_expr, ' or ') != -1:
            middle_pos = find_middle(string_expr, ' or ')
            func_name = 'func::logic_or'
            left_expr = generate_expression(string_expr[1: middle_pos])
            right_expr = generate_expression(string_expr[middle_pos + 4: -1])
        else:
            print(string_expr)
            assert False
        result_str = "[r['call'], cid_of['" + func_name + "'],\n[\n" + left_expr + ',\n' + right_expr + '\n]\n]'
        return result_str
    if find_middle(string_expr, ' == ', 0) != -1 \
            or find_middle(string_expr, ' === ', 0) != -1 \
            or find_middle(string_expr, ' > ', 0) != -1 \
            or find_middle(string_expr, ' < ', 0) != -1 \
            or find_middle(string_expr, ' >= ', 0) != -1 \
            or find_middle(string_expr, ' <= ', 0) != -1:
        func_name, left_expr, right_expr = None, None, None
        if find_middle(string_expr, ' == ', 0) != -1:
            # print(string_expr)
            middle_pos = find_middle(string_expr, ' == ', 0)
            func_name = 'func::compare_concepts'
            # print(string_expr[:middle_pos])
            # print(string_expr[middle_pos + 4:])
            left_expr = generate_expression(string_expr[:middle_pos])
            right_expr = generate_expression(string_expr[middle_pos + 4:])
        elif find_middle(string_expr, ' === ', 0) != -1:
            middle_pos = find_middle(string_expr, ' === ', 0)
            func_name = 'func::math_equal'
            left_expr = generate_expression(string_expr[: middle_pos])
            right_expr = generate_expression(string_expr[middle_pos + 5:])
        elif find_middle(string_expr, ' > ', 0) != -1:
            middle_pos = find_middle(string_expr, ' > ', 0)
            func_name = 'func::greater_than'
            left_expr = generate_expression(string_expr[: middle_pos])
            right_expr = generate_expression(string_expr[middle_pos + 3:])
        elif find_middle(string_expr, ' < ', 0) != -1:
            middle_pos = find_middle(string_expr, ' < ', 0)
            func_name = 'func::less_than'
            left_expr = generate_expression(string_expr[: middle_pos])
            right_expr = generate_expression(string_expr[middle_pos + 3:])
        elif find_middle(string_expr, ' >= ', 0) != -1:
            middle_pos = find_middle(string_expr, ' >= ', 0)
            func_name = 'func::greater_than_or_equal_to'
            left_expr = generate_expression(string_expr[: middle_pos])
            right_expr = generate_expression(string_expr[middle_pos + 4:])
        elif find_middle(string_expr, ' <= ', 0) != -1:
            middle_pos = find_middle(string_expr, ' <= ', 0)
            func_name = 'func::less_than_or_equal_to'
            left_expr = generate_expression(string_expr[: middle_pos])
            right_expr = generate_expression(string_expr[middle_pos + 4:])
        result_str = "[r['call'], cid_of['" + func_name + "'],\n[\n" + left_expr + ',\n' + right_expr + '\n]\n]'
        return result_str
    if find_middle(string_expr, ' != ', 0) != -1:
        middle_pos = find_middle(string_expr, ' != ', 0)
        left_expr = generate_expression(string_expr[: middle_pos])
        right_expr = generate_expression(string_expr[middle_pos + 4:])
        result_str = "[r['call'], cid_of['func::logic_not'], \n[\n[r['call'], cid_of['func::compare_concepts'],\n[\n" \
                     + left_expr + ',\n' + right_expr + "\n]\n]\n]]"
        return result_str
    if find_middle(string_expr, ' =!= ', 0) != -1:
        middle_pos = find_middle(string_expr, ' =!= ', 0)
        left_expr = generate_expression(string_expr[: middle_pos])
        right_expr = generate_expression(string_expr[middle_pos + 5:])
        result_str = "[r['call'], cid_of['func::logic_not'], \n[\n[r['call'], cid_of['func::math_equal'],\n[\n" \
                     + left_expr + ',\n' + right_expr + "\n]\n]\n]]"
        return result_str
    if string_expr.find('.find(') != -1 and\
            string_expr.find(' ', 0, string_expr.find('.find(')) == -1 and\
            string_expr.find('.find(') == rightest_naked_dot(string_expr):
        dot_pos = string_expr.find('.find(')
        target_expr = generate_expression(string_expr[: dot_pos])
        constraints_expr = generate_expression(string_expr[dot_pos + 6: -1])
        result_str = "[r['find'], " + target_expr + ', ' + constraints_expr + ']'
        return result_str
    if string_expr.find('.exist(') != -1 and\
            string_expr.find(' ', 0, string_expr.find('.exist(')) == -1 and\
            string_expr.find('.exist(') == rightest_naked_dot(string_expr):
        if not string_expr[-1] == ')':
            print('string_expr: ' + string_expr)
            assert False
        dot_pos = string_expr.find('.exist(')
        target_expr = generate_expression(string_expr[: dot_pos])
        constraints_expr = generate_expression(string_expr[dot_pos + 7: -1])
        result_str = "[r['exist'], " + target_expr + ', ' + constraints_expr + ']'
        return result_str
    if string_expr.find('.count(') != -1 and\
            string_expr.find(' ', 0, string_expr.find('.count(')) == -1 and\
            string_expr.find('.count(') == rightest_naked_dot(string_expr):
        assert string_expr[-1] == ')'
        dot_pos = string_expr.find('.count(')
        target_expr = generate_expression(string_expr[: dot_pos])
        constraints_expr = generate_expression(string_expr[dot_pos + 7: -1])
        result_str = "[r['count'], " + target_expr + ', ' + constraints_expr + ']'
        return result_str
    if string_expr.find('not ') == 0:
        target_expr = generate_expression(string_expr[4:])
        result_str = "[r['call'], cid_of['func::logic_not'], \n[\n" + target_expr + '\n]\n]'
        return result_str
    if string_expr.find('input') == 0 and string_expr[5:].isdigit():
        return "[r['input'], obj(" + string_expr[5:] + ')]'
    if string_expr.find('\'') == 0 and string_expr.find('\'', 1) != len(string_expr) - 1 \
            and string_expr[string_expr.find('\'', 1) + 1] == '(':
        assert string_expr[-1] == ')'
        end_quotation_pos = string_expr.find('\'', 1)
        function_name = string_expr[1: end_quotation_pos]
        if function_name not in cid_of.keys():
            print(function_name)
            assert False
        string_expr_copy = string_expr[end_quotation_pos + 2:]
        params = list()
        while string_expr_copy.find(', ') != -1:
            comma_pos = string_expr_copy.find(', ')
            params.append(generate_expression(string_expr_copy[:comma_pos]))
            string_expr_copy = string_expr_copy[comma_pos + 2:]
        params.append(generate_expression(string_expr_copy[:-1]))
        result_str = "[r['call'], cid_of['" + function_name + "'],\n[\n"
        for param in params:
            result_str += param + ',\n'
        result_str = result_str[:-2] + '\n]\n]'
        return result_str
    if string_expr[-1] == ']':
        open_bracket_pos = string_expr.find('[')
        if string_expr[open_bracket_pos + 1] == '!':
            is_reverse = True
            index = string_expr[open_bracket_pos + 2: -1]
        else:
            is_reverse = False
            index = generate_expression(string_expr[open_bracket_pos + 1: -1])
        target_expr = generate_expression(string_expr[: open_bracket_pos])
        if is_reverse:
            result_str = "[r['at_reverse'], " + target_expr + ', ' + index + ']'
        else:
            result_str = "[r['at'], " + target_expr + ', ' + index + ']'
        return result_str
    if string_expr.find('\'') == 0 and string_expr.find('\'', 1) == len(string_expr) - 1:
        assert string_expr[1:-1] in cid_of.keys()
        result_str = "[r['concept_instance'], cid_of['" + string_expr[1:-1] + "']]"
        return result_str
    if string_expr[-5:] == '.size' and string_expr.find(' ') == -1:
        target_expr = generate_expression(string_expr[:-5])
        result_str = "[r['size'], " + target_expr + ']'
        return result_str
    if find_middle(string_expr, '.\'', 0) != -1 and find_middle(string_expr, '.\'', 0) == rightest_naked_dot(string_expr):
        # print(string_expr)
        assert string_expr[-1] == '\''
        dot_pos = find_middle(string_expr, '.\'', 0)
        # print(string_expr[:dot_pos])
        # print(string_expr[dot_pos + 2:-1])
        target_expr = generate_expression(string_expr[:dot_pos])
        member = string_expr[dot_pos + 2:-1]
        if member not in cid_of.keys():
            print(member)
            assert False
        result_str = "[r['get_member'], " + target_expr + ", cid_of['" + member + "']]"
        return result_str
    if string_expr.find('reg') == 0 and string_expr.find(' ') == -1:
        if string_expr.find('<') != -1:
            assert string_expr[-1] == '>'
            assert string_expr.find('<>') == -1
            bracket_pos = string_expr.find('<')
            reg_id = string_expr[3: bracket_pos]
            string_expr_copy = string_expr
            string_expr_copy = string_expr_copy[bracket_pos + 1:]
            child_indices = list()
            while string_expr_copy.find(',') != -1:
                comma_pos = string_expr_copy.find(',')
                child_indices.append(generate_expression(string_expr_copy[:comma_pos]))
                string_expr_copy = string_expr_copy[comma_pos + 1:]
            child_indices.append(generate_expression(string_expr_copy[:-1]))
            result_str = "[r['reg'], obj(" + reg_id + '), ['
            assert child_indices
            for child_index in child_indices:
                result_str += child_index + ', '
            result_str = result_str[:-2]
            result_str += ']]'
        else:
            if not string_expr[3:].isdigit():
                raise AGIException('Something is wrong', special_name='expr', special_str=string_expr)
            reg_id = string_expr[3:]
            result_str = "[r['reg'], obj(" + reg_id + '), []]'
        return result_str
    if (len(string_expr) == 1 and string_expr in letter_to_number.keys()) or (
            string_expr.find('iter') == 0 and string_expr[4:].isdigit()):
        if len(string_expr) == 1:
            result_str = "[r['iterator'], obj(" + str(letter_to_number[string_expr]) + ')]'
        else:
            result_str = "[r['iterator'], obj(" + string_expr[4:] + ')]'
        return result_str
    if string_expr == 'target':
        result_str = "[r['target']]"
        return result_str
    if string_expr.isdigit():
        result_str = '[obj(' + string_expr + ')]'
        return result_str
    if string_expr == 'True' or 'False' or 'Fail':
        result_str = "[r['concept_instance'], cid_of['" + string_expr + "']]"
        return result_str
    return "['Unknown Expression']"


def count_indentation(line: str) -> int:
    line_copy = line
    count = 0
    while line_copy.find('    ') == 0:
        count += 1
        line_copy = line_copy[4:]
    return count


def get_current_line(string_code, current_index, indentation):
    line = string_code[current_index]
    for i in range(indentation):
        assert line.find('    ') == 0
        line = line[4:]
    return line


def generate_code_file(string_list_code, file_name, func_name):
    file = open(file_name, 'w')
    result = '''from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException
'''
    result += func_name + ' = '
    result += generate_code(slice_code(string_list_code))
    file.write(result)
    print('Succeeded!')
    file.close()


def generate_code(string_code: list) -> str:
    current_line_index = 0
    result = '[\n'
    current_line_copy = string_code[current_line_index]
    indentation_count = 0
    while current_line_copy.find('    ') == 0:
        indentation_count += 1
        current_line_copy = current_line_copy[4:]

    while current_line_index < len(string_code):
        current_line = get_current_line(string_code, current_line_index, indentation_count)
        print(current_line)
        if current_line.find(' = ') != -1 or current_line.find(' &= ') != -1:
            if current_line.find(' = ') != -1:
                assign_pos = current_line.find(' = ')
                current_line_code = "[r['assign'], "
            else:
                assign_pos = current_line.find(' &= ')
                current_line_code = "[r['assign_as_reference'], "
            left_expr = generate_expression(current_line[:assign_pos])
            if current_line.find(' = ') != -1:
                right_expr = generate_expression(current_line[assign_pos + 3:])
            else:
                right_expr = generate_expression(current_line[assign_pos + 4:])
            current_line_code += left_expr + ', ' + right_expr + ']'
            result += current_line_code + ', \n'
            current_line_index += 1
        elif current_line.find('return ') == 0:
            return_expr = generate_expression(current_line[7:])
            current_line_code = "[r['return'], " + return_expr + ']'
            result += current_line_code + ', \n'
            current_line_index += 1
        elif current_line.find('assert ') == 0:
            assert_expr = generate_expression(current_line[7:])
            current_line_code = "[r['assert'], " + assert_expr + ']'
            result += current_line_code + ', \n'
            current_line_index += 1
        elif current_line.find('for ') == 0:
            in_pos = current_line.find(' in range(')
            iter_str = current_line[4: in_pos]
            if len(iter_str) == 1:
                assert iter_str in letter_to_number.keys()
                iter_index = letter_to_number[iter_str]
            else:
                assert iter_str.find('iter') == 0
                iter_index = int(iter_str[4:])
            iter_expr = 'obj(' + str(iter_index) + ')'
            bracket_pos = current_line.find('):')
            end_value_expr = generate_expression(current_line[in_pos + 10: bracket_pos])
            current_line_code = "[r['for'], " + iter_expr + ', ' + end_value_expr + ',\n'
            current_line_index += 1
            for_lines = list()
            if current_line_index == len(string_code):
                raise AGIException('Unexpected ending of code.')
            current_line = get_current_line(string_code, current_line_index, indentation_count)
            while count_indentation(current_line) >= 1:
                for_lines.append(current_line)
                current_line_index += 1
                if current_line_index == len(string_code):
                    break
                current_line = get_current_line(string_code, current_line_index, indentation_count)
            current_line_code += generate_code(for_lines) + '\n]'
            result += current_line_code + ', \n'
        elif current_line.find('while ') == 0:
            while_expr = generate_expression(current_line[6: -1])
            current_line_code = "[r['while'], " + while_expr + ',\n'
            current_line_index += 1
            while_lines = list()
            if current_line_index == len(string_code):
                raise AGIException('Unexpected ending of code.')
            current_line = get_current_line(string_code, current_line_index, indentation_count)
            while count_indentation(current_line) >= 1:
                while_lines.append(current_line)
                current_line_index += 1
                if current_line_index == len(string_code):
                    break
                current_line = get_current_line(string_code, current_line_index, indentation_count)
            current_line_code += generate_code(while_lines) + '\n]'
            result += current_line_code + ', \n'
        elif current_line == 'break':
            current_line_code = "[r['break']]"
            result += current_line_code + ', \n'
            current_line_index += 1
        elif current_line.find('if ') == 0:
            if_expr = generate_expression(current_line[3: -1])
            current_line_code = "[r['if'], " + if_expr + ',\n'
            current_line_index += 1
            if_lines = list()
            if current_line_index == len(string_code):
                raise AGIException('Unexpected ending of code.', special_name='line',
                                   special_str=str(current_line_index))
            current_line = get_current_line(string_code, current_line_index, indentation_count)
            while count_indentation(current_line) >= 1:
                if_lines.append(current_line)
                current_line_index += 1
                if current_line_index == len(string_code):
                    break
                current_line = get_current_line(string_code, current_line_index, indentation_count)
            current_line_code += generate_code(if_lines) + ',\n['
            if current_line_index != len(string_code):
                current_line = get_current_line(string_code, current_line_index, indentation_count)
                has_elif_block = False
                while current_line.find('elif ') == 0:
                    has_elif_block = True
                    elif_expr = generate_expression(current_line[5:-1])
                    current_line_index += 1
                    elif_lines = list()
                    if current_line_index == len(string_code):
                        raise AGIException('Unexpected ending of code.')
                    current_line = get_current_line(string_code, current_line_index, indentation_count)
                    while count_indentation(current_line) >= 1:
                        elif_lines.append(current_line)
                        current_line_index += 1
                        if current_line_index == len(string_code):
                            break
                        current_line = get_current_line(string_code, current_line_index, indentation_count)
                    current_line_code += '[\n' + elif_expr + ',\n' + generate_code(elif_lines) + '\n],\n'
                if has_elif_block:
                    current_line_code = current_line_code[: -2]
                current_line_code += '],\n'
                has_else = False
                if current_line_index != len(string_code):
                    current_line = get_current_line(string_code, current_line_index, indentation_count)
                    if current_line == 'else:':
                        has_else = True
                        current_line_index += 1
                        else_lines = list()
                        if current_line_index == len(string_code):
                            raise AGIException('Unexpected ending of code.')
                        current_line = get_current_line(string_code, current_line_index, indentation_count)
                        while count_indentation(current_line) >= 1:
                            else_lines.append(current_line)
                            current_line_index += 1
                            if current_line_index == len(string_code):
                                break
                            current_line = get_current_line(string_code, current_line_index, indentation_count)
                        current_line_code += generate_code(else_lines) + '\n'
                if not has_else:
                    current_line_code += '[]\n'
                current_line_code += ']'
            else:
                current_line_code += '],\n[]\n]'
            result += current_line_code + ', \n'
        elif current_line.find('.append(') != -1:
            append_pos = current_line.find('.append(')
            left_expr = generate_expression(current_line[: append_pos])
            right_expr = generate_expression(current_line[append_pos + 8:-1])
            assert (current_line[-1] == ')')
            current_line_code = "[r['append'], " + left_expr + ', ' + right_expr + ']'
            result += current_line_code + ', \n'
            current_line_index += 1
        elif current_line.find('.remove(') != -1:
            append_pos = current_line.find('.remove(')
            left_expr = generate_expression(current_line[: append_pos])
            right_expr = generate_expression(current_line[append_pos + 8:-1])
            assert (current_line[-1] == ')')
            current_line_code = "[r['remove'], " + left_expr + ', ' + right_expr + ']'
            result += current_line_code + ', \n'
            current_line_index += 1
        elif current_line.find('request ') == 0:
            assert current_line.find('s.t.{') != -1
            current_line_copy = current_line
            current_line_copy = current_line_copy[8:]
            assert current_line_copy.find('reg') == 0
            reg_ids = list()
            while current_line_copy.find('reg') == 0:
                comma_pos = current_line_copy.find(', ')
                assert comma_pos != -1
                reg_id = int(current_line_copy[3: comma_pos])
                reg_ids.append(reg_id)
                current_line_copy = current_line_copy[comma_pos + 2:]
            assert current_line_copy.find('s.t.{') == 0
            subject_to_pos = current_line.find('s.t.{')
            assert subject_to_pos != -1
            provided_pos = current_line.find('}, provided:')
            assert provided_pos != -1
            constraints_expr = generate_expression(current_line[subject_to_pos + 5: provided_pos])
            current_line_code = "[r['request'],\n["
            assert reg_ids
            for reg_id in reg_ids:
                current_line_code += 'obj(' + str(reg_id) + '), '
            current_line_code = current_line_code[:-2] + '],\n' + constraints_expr + ',\n'
            result += current_line_code
            current_line_index += 1
            if current_line_index == len(string_code):
                raise AGIException('Unexpected ending of code.')
            current_line = get_current_line(string_code, current_line_index, indentation_count)
            provided_lines = list()
            while count_indentation(current_line) >= 1:
                provided_lines.append(current_line)
                current_line_index += 1
                if current_line_index == len(string_code):
                    break
                current_line = get_current_line(string_code, current_line_index, indentation_count)
            assert provided_lines
            result += generate_code(provided_lines) + '\n], \n'
        elif current_line.find('\'') == 0:
            assert current_line[-1] == ')'
            end_quotation_pos = current_line.find('\'', 1)
            assert current_line[end_quotation_pos+1] == '('
            code_name = current_line[1: end_quotation_pos]
            assert code_name in cid_of.keys()
            params = list()
            current_line_copy = current_line[end_quotation_pos + 2]
            while current_line_copy.find(', ') != -1:
                comma_pos = current_line_copy.find(', ')
                params.append(generate_expression(current_line_copy[:comma_pos]))
            if current_line_copy[0] != ')':
                params.append(generate_expression(current_line_copy[:-1]))
            result = "[r['call_none_return_func'], cid_of['" + code_name + "'],\n[\n"
            for param in params:
                result += param + ',\n'
            if params:
                result = result[:-2]
            result += '\n]\n]'
        elif current_line == '':
            current_line_index += 1
        else:
            raise AGIException('Unknown text.')
    assert result[-1] == '\n'
    result = result[:-3]
    result += '\n]'
    return result
