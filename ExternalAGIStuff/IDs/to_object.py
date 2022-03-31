from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject, AGIList
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from exception import AGIException


def obj(target: int or bool or str) -> AGIObject:
    if type(target) == int:
        number_str = str(target)
        object_list = []
        for digit in number_str:
            object_list.append(AGIObject(cid_of[digit], dict()))
        return AGIObject(cid_of['natural_number'], {cid_of['content']: AGIList(object_list)})
    elif type(target) == bool:
        if target:
            return AGIObject(cid_of['True'], dict())
        else:
            return AGIObject(cid_of['False'], dict())
    elif type(target) == str:
        assert target in cid_of.keys()
        return AGIObject(cid_of[target], dict())


def to_integer(natural_number: AGIObject) -> int:
    if type(natural_number) != AGIObject:
        raise AGIException('Expect AGIObject', special_name='type', special_str=str(type(natural_number)))
    if natural_number.concept_id != cid_of['natural_number']:
        raise AGIException('Expect natural number')
    integer_str = str()
    for i in range(natural_number.attributes[cid_of['content']].size()):
        digit_obj = natural_number.attributes[cid_of['content']].get_element(i)
        digit_id = digit_obj.concept_id
        if digit_id == cid_of['0']:
            integer_str += '0'
        elif digit_id == cid_of['1']:
            integer_str += '1'
        elif digit_id == cid_of['2']:
            integer_str += '2'
        elif digit_id == cid_of['3']:
            integer_str += '3'
        elif digit_id == cid_of['4']:
            integer_str += '4'
        elif digit_id == cid_of['5']:
            integer_str += '5'
        elif digit_id == cid_of['6']:
            integer_str += '6'
        elif digit_id == cid_of['7']:
            integer_str += '7'
        elif digit_id == cid_of['8']:
            integer_str += '8'
        elif digit_id == cid_of['9']:
            integer_str += '9'
        else:
            raise AGIException('Unexpected thing as digit.', special_name='thing', special_str=str(cid_reverse[digit_id]))
    return int(integer_str)


def to_str(thing: AGIObject):
    if thing.concept_id == cid_of['natural_number']:
        if thing.attributes[cid_of['content']] is None:
            return 'empty_natural_number'
        return str(to_integer(thing))
    return cid_reverse[thing.concept_id]


def translate_input(str_input) -> AGIObject:
    return obj(int(str_input))
