from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject, AGIList, get_agi_list
from ExternalAGIStuff.IDs.to_object import to_integer, obj
from ExternalAGIStuff.HardcodedFunctions.hardcoded_function_ids import hardcoded_function_linker
from ExternalAGIStuff.IDs.concept_ids import cid_of


# input0: code_id
def is_code_dynamic(params: list):
    assert type(params[0]) == AGIObject
    code_id = params[0].concept_id
    if code_id == cid_of['func::run_hardcoded_code']:
        return obj(False)
    if code_id == cid_of['func::is_code_dynamic']:
        return obj(False)
    if code_id in hardcoded_function_linker.keys():
        return obj(False)
    return obj(True)
