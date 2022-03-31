from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject, AGIList
from exception import AGIException


def translate_AGIList(agi_list: AGIList, indentation=0, attribute_name=str()):
    result = str()
    for i in range(indentation):
        result += '|   '
    if attribute_name != '':
        result += "'" + attribute_name + "': "
    result += 'AGIList\n'
    for i in agi_list.get_list():
        if type(i) == AGIObject:
            result += translate_AGIObject(i, indentation + 1)
        elif type(i) == AGIList():
            result += translate_AGIList(i, indentation + 1)
        elif type(i) is None:
            for j in range(indentation + 1):
                result += '    '
            result += 'None\n'
        else:
            raise AGIException('Unexpected type.')
    return result


def translate_AGIObject(agi_object: AGIObject, indentation=0, attribute_name=str()):
    result = str()
    for i in range(indentation):
        result += '|   '
    if attribute_name != '':
        result += "'" + attribute_name + "': "
    result += "'" + cid_reverse[agi_object.concept_id] + "'\n"
    for i in agi_object.attributes:
        if type(agi_object.attributes[i]) == AGIObject:
            result += translate_AGIObject(agi_object.attributes[i], indentation + 1, cid_reverse[i])
        elif type(agi_object.attributes[i]) == AGIList:
            result += translate_AGIList(agi_object.attributes[i], indentation + 1, cid_reverse[i])
        elif agi_object.attributes[i] is None:
            for j in range(indentation + 1):
                result += '|   '
            result += "'" + cid_reverse[i] + '\': None\n'
        else:
            print(cid_reverse[agi_object.attributes[i]])
            raise AGIException('Unexpected type.', special_name='type', special_str=str(type(agi_object.attributes[i])))
    return result
