from ExternalAGIStuff.IDs.concept_ids import cid_of
from ExternalAGIStuff.FundamentalCode.numeral_code import *
from ExternalAGIStuff.TestCode.test_code1 import *
from ExternalAGIStuff.FundamentalCode.batch_code import *
code_dict = {
    cid_of['func::compare_natural_numbers']: compare_natural_numbers_code,
    cid_of['func::digit_to_natural_number']: digit_to_natural_number_code,
    cid_of['func::greater_than']: greater_than_code,
    cid_of['func::less_than']: less_than_code,
    cid_of['func::greater_than_or_equal_to']: greater_than_or_equal_to_code,
    cid_of['func::less_than_or_equal_to']: less_than_or_equal_to_code,
    cid_of['func::math_equal']: math_equal_code,
    cid_of['func::test_code']: test_code4,
    cid_of['func::batch_logic_and']: batch_logic_and,
    cid_of['func::batch_logic_or']: batch_logic_or,
    cid_of['func::max']: max_code,
    cid_of['func::min']: min_code
}


def get_code(code_id) -> list:
    global code_dict
    return code_dict[code_id]

