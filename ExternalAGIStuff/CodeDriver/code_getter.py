from ExternalAGIStuff.IDs.concept_ids import cid_of
from ExternalAGIStuff.FundamentalCode.numeral_code import *
code_dict = {
    cid_of['func::compare_natural_numbers']: compare_natural_numbers_code,
    cid_of['func::digit_to_natural_number']: digit_to_natural_number_code
}


def get_code(code_id) -> list:
    global code_dict
    return code_dict[code_id]

