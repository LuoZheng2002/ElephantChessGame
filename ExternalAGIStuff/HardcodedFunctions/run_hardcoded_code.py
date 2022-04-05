from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject, AGIList, get_agi_list
from ExternalAGIStuff.HardcodedFunctions.hardcoded_function_ids import hardcoded_function_linker
from ExternalAGIStuff.IDs.concept_ids import cid_of
from ExternalAGIStuff.HardcodedFunctions.is_code_dynamic import is_code_dynamic
# input0: code_id, input1: params
def run_hardcoded_code(params: list):
    assert type(params[0]) == AGIObject
    code_id = params[0].concept_id
    function_params = params[1]
    if type(function_params) == AGIObject:
        function_params = get_agi_list(function_params)
    assert type(function_params) == AGIList
    assert code_id in hardcoded_function_linker.keys() or code_id == cid_of['func::run_hardcoded_code'] or code_id == cid_of['func::is_code_dynamic']
    if code_id == cid_of['func::run_hardcoded_code']:
        return run_hardcoded_code(function_params.get_list())
    elif code_id == cid_of['func::is_code_dynamic']:
        return is_code_dynamic(function_params.get_list())
    return hardcoded_function_linker[code_id](function_params.get_list())


