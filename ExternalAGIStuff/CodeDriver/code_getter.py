from ExternalAGIStuff.IDs.concept_ids import cid_of
from ExternalAGIStuff.FundamentalCode.numeral_code import *
from ExternalAGIStuff.TestCode.test_code1 import *
from ExternalAGIStuff.FundamentalCode.batch_code import *
from ExternalAGIStuff.FundamentalCode.Formatted.child_indices_equal_f import child_indices_equal_f
from ExternalAGIStuff.FundamentalCode.Formatted.run_dynamic_code_object_f import run_dynamic_code_object_f
from ExternalAGIStuff.FundamentalCode.Formatted.remove_one_element_f import remove_one_element_f
from ExternalAGIStuff.FundamentalCode.Formatted.increment_f import increment_f
from ExternalAGIStuff.FundamentalCode.Formatted.process_line_f import process_line_f
from ExternalAGIStuff.FundamentalCode.Formatted.solve_expression_f import solve_expression_f
from generate_code import test
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
    cid_of['func::min']: min_code,
    cid_of['func::child_indices_equal']: child_indices_equal_f,
    cid_of['func::run_dynamic_code_object']: run_dynamic_code_object_f,
    cid_of['func::remove_one_element']: remove_one_element_f,
    cid_of['func::increment']: increment_f,
    cid_of['func::process_line']: process_line_f,
    cid_of['func::solve_expression']: solve_expression_f,
    cid_of['func::test']: test,
}


def get_code(code_id) -> list:
    global code_dict
    return code_dict[code_id]

