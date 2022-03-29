from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from code_browser import letter_to_number
from exception import AGIException


def generate_expression(string_expr: str) -> str:
    return '["AN EXPRESSION"]'


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


def generate_code(string_code: list) -> str:
    current_line_index = 0
    result = '['
    current_line_copy = string_code[current_line_index]
    indentation_count = 0
    while current_line_copy.find('    ') == 0:
        indentation_count += 1
        current_line_copy = current_line_copy[4:]
    
    while current_line_index < len(string_code):
        current_line = get_current_line(string_code, current_line_index, indentation_count)
        while current_line.find('    ') == 0:
            current_line = current_line[4:]

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
            current_line_code = "[r['for'], " + iter_expr + ', ' + end_value_expr + ', '
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
            current_line_code += generate_code(for_lines) + ']'
            result += current_line_code + ', \n'
        elif current_line.find('while ') == 0:
            while_expr = generate_expression(current_line[6: -1])
            current_line_code = "[r['while'], " + while_expr + ', '
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
            current_line_code += generate_code(while_lines) + ']'
            result += current_line_code + ', \n'
        elif current_line == 'break':
            current_line_code = "[r['break']]"
            result += current_line_code + ', \n'
            current_line_index += 1
        elif current_line.find('if ') == 0:
            if_expr = generate_expression(current_line[3: -1])
            current_line_code = "[r['if'], " + if_expr + ', '
            current_line_index += 1
            if_lines = list()
            if current_line_index == len(string_code):
                raise AGIException('Unexpected ending of code.', special_name='line', special_str=str(current_line_index))
            current_line = get_current_line(string_code, current_line_index, indentation_count)
            while count_indentation(current_line) >= 1:
                if_lines.append(current_line)
                current_line_index += 1
                if current_line_index == len(string_code):
                    break
                current_line = get_current_line(string_code, current_line_index, indentation_count)
            current_line_code += generate_code(if_lines) + ', ['
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
                    current_line_code += '[' + elif_expr + ', ' + generate_code(elif_lines) + '], '
                if has_elif_block:
                    current_line_code = current_line_code[: -2]
                current_line_code += '], '
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
                        current_line_code += generate_code(else_lines)
                if not has_else:
                    current_line_code += '[]'
                current_line_code += ']'
            else:
                current_line_code += '], []]'
            result += current_line_code + ', \n'
        elif current_line.find('.append(') != -1:
            append_pos = current_line.find('.append(')
            left_expr = generate_expression(current_line[: append_pos])
            right_expr = generate_expression(current_line[append_pos + 8, -1])
            assert(current_line[-1] == ')')
            current_line_code = "[r['append'], " + left_expr + ', ' + right_expr + ']'
            result += current_line_code + ', \n'
            current_line_index += 1
        elif current_line.find('.remove(') != -1:
            append_pos = current_line.find('.remove(')
            left_expr = generate_expression(current_line[: append_pos])
            right_expr = generate_expression(current_line[append_pos + 8, -1])
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
            assert current_line[-1] == '}'
            subject_to_pos = current_line.find('s.t.{')
            assert subject_to_pos != -1
            constraints_expr = generate_expression(current_line[subject_to_pos + 5: -1])
            current_line_code = "[r['request'], ["
            assert reg_ids
            for reg_id in reg_ids:
                current_line_code += 'obj(' + str(reg_id) + '), '
            current_line_code = current_line_code[:-2] + '], ' + constraints_expr + ']'
            result += current_line_code + ', \n'
            current_line_index += 1
    assert result[-1] == '\n'
    result = result[:-3]
    result += ']'
    return result

