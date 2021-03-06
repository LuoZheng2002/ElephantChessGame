from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject, AGIList, get_agi_list
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from exception import AGIException
from ExternalAGIStuff.IDs.to_object import to_integer, obj
from ExternalAGIStuff.CodeDriver.code_getter import code_dict, get_code
from ExternalAGIStuff.code_to_object import code_to_object
from ExternalAGIStuff.CodeDriver.concept_instance_creator import concept_attributes_dict

def compare_concepts(params: list) -> AGIObject:
    if len(params) != 2:
        raise AGIException('Function should receive 2 params.')
    param1 = params[0]
    param2 = params[1]
    if type(param1) != AGIObject or type(param2) != AGIObject:
        raise AGIException('Parameters should be AGIObjects.', special_name='type',
                           special_str=str(cid_reverse[param2.concept_id]))
    if param1.concept_id == param2.concept_id:
        return AGIObject(cid_of['True'], dict())
    else:
        return AGIObject(cid_of['False'], dict())


def logic_and(params: list) -> AGIObject:
    if len(params) != 2:
        raise AGIException('logic_and function should receive 2 params.')
    param1 = params[0]
    param2 = params[1]
    if type(param1) != AGIObject or type(param2) != AGIObject:
        raise AGIException('Parameters should be AGIObjects.')
    if (param1.concept_id != cid_of['True'] and param1.concept_id != cid_of['False'] and param1.concept_id != cid_of[
        'Fail']) or \
            (param2.concept_id != cid_of['True'] and param2.concept_id != cid_of['False'] and param2.concept_id !=
             cid_of['Fail']):
        raise AGIException('Invalid parameters in logic_and function.')
    if param1.concept_id == cid_of['False'] or param2.concept_id == cid_of['False']:
        return AGIObject(cid_of['False'], dict())
    elif param1.concept_id == cid_of['Fail'] or param2.concept_id == cid_of['Fail']:
        return AGIObject(cid_of['Fail'], dict())
    else:
        return AGIObject(cid_of['True'], dict())


def logic_or(params: list) -> AGIObject:
    if len(params) != 2:
        raise AGIException('logic_and function should receive 2 params.')
    param1 = params[0]
    param2 = params[1]
    if type(param1) != AGIObject or type(param2) != AGIObject:
        raise AGIException('Parameters should be AGIObjects.')
    if (param1.concept_id != cid_of['True'] and param1.concept_id != cid_of['False'] and param1.concept_id != cid_of[
        'Fail']) or \
            (param2.concept_id != cid_of['True'] and param2.concept_id != cid_of['False'] and param2.concept_id !=
             cid_of['Fail']):
        raise AGIException('Invalid parameters in logic_and function.')
    if param1.concept_id == cid_of['True'] or param2.concept_id == cid_of['True']:
        return AGIObject(cid_of['True'], dict())
    elif param1.concept_id == cid_of['Fail'] or param2.concept_id == cid_of['Fail']:
        return AGIObject(cid_of['Fail'], dict())
    else:
        return AGIObject(cid_of['False'], dict())


def logic_not(params: list) -> AGIObject:
    if len(params) != 1:
        raise AGIException('logic_not function should receive 1 param.')
    param = params[0]
    if type(param) != AGIObject:
        print(param)
        raise AGIException('Parameters should be AGIObjects.')
    if param.concept_id != cid_of['True'] and param.concept_id != cid_of['False']\
            and param.concept_id != cid_of['Fail']:
        raise AGIException('Invalid parameter in logic_not function.')
    if param.concept_id == cid_of['Fail']:
        return AGIObject(cid_of['Fail'], dict())
    elif param.concept_id == cid_of['True']:
        return AGIObject(cid_of['False'], dict())
    else:
        return AGIObject(cid_of['True'], dict())


def is_natural_number_single_digit(params: list) -> AGIObject:
    if len(params) != 1:
        raise AGIException('This function should receive 1 param.')
    param = params[0]
    if type(param) != AGIObject:
        raise AGIException('Parameters should be AGIObjects.')
    if param.concept_id == cid_of['Fail']:
        return obj('Fail')
    if param.concept_id != cid_of['natural_number']:
        raise AGIException('Parameter should be natural number.')
    if param.attributes[cid_of['content']].size() == 1:
        return AGIObject(cid_of['True'], dict())
    else:
        return AGIObject(cid_of['False'], dict())


# ??????????????????????????????
def compare_single_digit_natural_numbers(params: list) -> AGIObject:
    if len(params) != 2:
        raise AGIException('This function should receive 2 params.')
    param1 = params[0]
    param2 = params[1]
    if type(param1) != AGIObject or type(param2) != AGIObject:
        raise AGIException('Parameters should be AGIObjects.')
    if param1.concept_id == cid_of['Fail'] or param2.concept_id == cid_of['Fail']:
        return obj('Fail')
    if param1.concept_id != cid_of['natural_number'] or param2.concept_id != cid_of['natural_number']:
        raise AGIException('Parameters should be natural numbers.')
    if param1.attributes[cid_of['content']].size() != 1 or param2.attributes[cid_of['content']].size() != 1:
        raise AGIException('Parameters should be single-digit.')
    digits = [None, None]
    digits[0] = param1.attributes[cid_of['content']].get_element(0)
    digits[1] = param2.attributes[cid_of['content']].get_element(0)
    integers = [None, None]
    for i in range(2):
        if digits[i].concept_id == cid_of['0']:
            integers[i] = 0
        elif digits[i].concept_id == cid_of['1']:
            integers[i] = 1
        elif digits[i].concept_id == cid_of['2']:
            integers[i] = 2
        elif digits[i].concept_id == cid_of['3']:
            integers[i] = 3
        elif digits[i].concept_id == cid_of['4']:
            integers[i] = 4
        elif digits[i].concept_id == cid_of['5']:
            integers[i] = 5
        elif digits[i].concept_id == cid_of['6']:
            integers[i] = 6
        elif digits[i].concept_id == cid_of['7']:
            integers[i] = 7
        elif digits[i].concept_id == cid_of['8']:
            integers[i] = 8
        elif digits[i].concept_id == cid_of['9']:
            integers[i] = 9
        else:
            raise AGIException('Unexpected element as digit.')
    if integers[0] < integers[1]:
        return AGIObject(cid_of['less_than'], dict())
    elif integers[0] == integers[1]:
        return AGIObject(cid_of['math_equal'], dict())
    else:
        return AGIObject(cid_of['greater_than'], dict())


def sum_func(params: list) -> AGIObject:
    if len(params) != 2:
        raise AGIException('This function should receive 2 params.')
    param1 = params[0]
    param2 = params[1]
    if type(param1) != AGIObject or type(param2) != AGIObject:
        raise AGIException('Parameters should be AGIObjects.')
    if param1.concept_id == cid_of['Fail'] or param2.concept_id == cid_of['Fail']:
        return obj('Fail')
    if param1.concept_id != cid_of['natural_number'] or param2.concept_id != cid_of['natural_number']:
        raise AGIException('Parameters should be natural numbers.')
    number1 = to_integer(param1)
    number2 = to_integer(param2)
    return obj(number1 + number2)


def difference_func(params: list) -> AGIObject:
    if len(params) != 2:
        raise AGIException('This function should receive 2 params.')
    param1 = params[0]
    param2 = params[1]
    if type(param1) != AGIObject or type(param2) != AGIObject:
        raise AGIException('Parameters should be AGIObjects.')
    if param1.concept_id == cid_of['Fail'] or param2.concept_id == cid_of['Fail']:
        return obj('Fail')
    if param1.concept_id != cid_of['natural_number'] or param2.concept_id != cid_of['natural_number']:
        raise AGIException('Parameters should be natural numbers.')
    number1 = to_integer(param1)
    number2 = to_integer(param2)
    if number1 - number2 < 0:
        return AGIObject(cid_of['Fail'], dict())
    return obj(number1 - number2)


# params[0]: object, params[1]: member object
def get_object_member_func(params: list) -> AGIObject:
    target_object = params[0]
    member_object = params[1]
    assert type(target_object) == AGIObject and type(member_object) == AGIObject
    assert member_object.concept_id in target_object.attributes.keys()
    return target_object.attributes[member_object.concept_id]


# params[0]: object, params[1]: member object, params[2]: value
def set_object_member_func(params: list):
    target_object = params[0]
    member_object = params[1]
    value = params[2]
    assert type(target_object) == AGIObject and type(member_object) == AGIObject
    assert member_object.concept_id in target_object.attributes.keys()
    target_object.attributes[member_object.concept_id] = value


#
def remove_element_by_index(params: list):
    target_list = params[0]
    index = params[1]
    if type(target_list) == AGIObject:
        target_list = get_agi_list(target_list)
    assert type(target_list) == AGIList
    if target_list.size() == 0:
        raise AGIException('empty list', special_name='index', special_str=str(to_integer(index)))
    target_list.remove(to_integer(index))


def get_input_object(params: list):
    input_object = obj(int(input('Dynamic code simulator asks you to input one param.\n')))
    return input_object



def get_dynamic_code_object(params: list):
    assert type(params[0]) == AGIObject
    code_id = params[0].concept_id
    assert code_id in code_dict.keys()
    return code_to_object(get_code(code_id))


def create_concept_instance_func(params: list):
    assert type(params[0]) == AGIObject
    concept_id = params[0].concept_id
    if concept_id not in concept_attributes_dict.keys():
        return AGIObject(concept_id, dict())
    else:
        attributes = dict()
        for i in concept_attributes_dict[concept_id]:
            attributes.update({i: None})
        return AGIObject(concept_id, attributes)
