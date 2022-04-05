from ExternalAGIStuff.HardcodedFunctions.hardcoded_functions import *
hardcoded_function_linker = {
    cid_of['func::compare_concepts']: compare_concepts,
    cid_of['func::logic_and']: logic_and,
    cid_of['func::logic_or']: logic_or,
    cid_of['func::logic_not']: logic_not,
    cid_of['func::is_natural_number_single_digit']: is_natural_number_single_digit,
    cid_of['func::compare_single_digit_natural_numbers']: compare_single_digit_natural_numbers,
    cid_of['func::sum']: sum_func,
    cid_of['func::difference']: difference_func,
    cid_of['func::get_object_member']: get_object_member_func,
    cid_of['func::set_object_member']: set_object_member_func,
    cid_of['func::remove_element_by_index']: remove_element_by_index,
    cid_of['func::get_input_object']: get_input_object,
    cid_of['func::get_dynamic_code_object']: get_dynamic_code_object,
}
