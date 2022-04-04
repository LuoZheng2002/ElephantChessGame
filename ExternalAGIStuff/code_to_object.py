from exception import AGIException
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject, AGIList
from copy import deepcopy
from ExternalAGIStuff.CodeDriver.runtime_memory import ResourceManager
from ExternalAGIStuff.IDs.reserved_keywords import r, rr
from ExternalAGIStuff.CodeDriver.concept_instance_creator import create_concept_instance
from ExternalAGIStuff.CodeDriver.code_getter import get_code
from ExternalAGIStuff.HardcodedFunctions.hardcoded_function_ids import hardcoded_function_linker
from ExternalAGIStuff.IDs.to_object import obj, to_integer, to_str, translate_input
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeVisualization.code_browser import visualize_line
from debug import dout, debug_on, debug_on_all


def pack_expr(expr: list) -> AGIObject:
    if len(expr) == 1 and type(expr[0]) != int:
        return AGIObject(cid_of['dcr::constexpr'],
                         {cid_of['content']: expr[0]})
    head = expr[0]
    if head == r['input']:
        result = AGIObject(cid_of['dcr::input'],
                           {cid_of['dc::index']: expr[1]})
    elif head == r['reg']:
        result = AGIObject(cid_of['dcr::reg'],
                           {cid_of['dc::index']: expr[1],
                            cid_of['dc::child_indices']: pack_list(expr[2], 'expr')})
    elif head == r['iterator']:
        result = AGIObject(cid_of['dcr::iterator'],
                           {cid_of['dc::index']: expr[1]})
    elif head == r['call']:
        result = AGIObject(cid_of['dcr::call'],
                           {cid_of['dc::function_name']: AGIObject(expr[1]),
                            cid_of['dc::function_params']: pack_list(expr[2], 'expr')})
    elif head == r['concept_instance']:
        result = AGIObject(cid_of['dcr::concept_instance'],
                           {cid_of['dc::concept_name']: AGIObject(expr[1])})
    elif head == r['size']:
        result = AGIObject(cid_of['dcr::size'],
                           {cid_of['dc::target_list']: pack_expr(expr[1])})
    elif head == r['get_member']:
        result = AGIObject(cid_of['dcr::get_member'],
                           {cid_of['dc::target_object']: pack_expr(expr[1]),
                            cid_of['dc::member_name']: AGIObject(expr[2])})
    elif head == r['at']:
        result = AGIObject(cid_of['dcr::at'],
                           {cid_of['dc::target_list']: pack_expr(expr[1]),
                            cid_of['dc::index']: pack_expr(expr[2])})
    elif head == r['at_reverse']:
        result = AGIObject(cid_of['dcr::at_reverse'],
                           {cid_of['dc::target_list']: pack_expr(expr[1]),
                            cid_of['dc::index']: pack_expr(expr[2])})
    elif head == r['find']:
        result = AGIObject(cid_of['dcr::find'],
                           {cid_of['dc::target_list']: pack_expr(expr[1]),
                            cid_of['dc::expression_for_constraint']: pack_expr(expr[2])})
    elif head == r['exist']:
        result = AGIObject(cid_of['dcr::exist'],
                           {cid_of['dc::target_list']: pack_expr(expr[1]),
                            cid_of['dc::expression_for_constraint']: pack_expr(expr[2])})
    elif head == r['count']:
        result = AGIObject(cid_of['dcr::count'],
                           {cid_of['dc::target_list']: pack_expr(expr[1]),
                            cid_of['dc::expression_for_constraint']: pack_expr(expr[2])})
    elif head == r['target']:
        result = AGIObject(cid_of['dcr::target'])
    else:
        raise AGIException('Unexpected head.')
    return result


def pack_sub_block(sub_block: list) -> AGIObject:
    lines = list()
    for line in sub_block:
        line_obj = pack_line(line)
        lines.append(line_obj)
    result = AGIObject(cid_of['dc::sub_block'], {cid_of['dc::lines']: AGIList(lines)})

    return result


def pack_list(list_param: list, list_type) -> AGIList:
    list_result = list()
    if list_type == 'expr':
        for param in list_param:
            list_result.append(pack_expr(param))
    elif list_type == 'elif':
        for param in list_param:
            module_object = AGIObject(cid_of['dc::elif_module'],
                                      {cid_of['dc::expression_for_judging']: pack_expr(param[0]),
                                       cid_of['dc::elif_block']: pack_sub_block(param[1])})
            list_result.append(module_object)
    elif list_type == 'number':
        for param in list_param:
            list_result.append(param)
    else:
        raise AGIException('Unexpected list_type')
    return AGIList(list_result)


def pack_line(line: list) -> AGIObject:
    head = line[0]
    if head == r['assign']:
        result = AGIObject(cid_of['dcr::assign'],
                           {cid_of['dc::left_value']: pack_expr(line[1]),
                            cid_of['dc::right_value']: pack_expr(line[2])})
    elif head == r['assign_as_reference']:
        result = AGIObject(cid_of['dcr::assign_as_reference'],
                           {cid_of['dc::left_value']: pack_expr(line[1]),
                            cid_of['dc::right_value']: pack_expr(line[2])})
    elif head == r['return']:
        result = AGIObject(cid_of['dcr::return'],
                           {cid_of['dc::return_value']: pack_expr(line[1])})
    elif head == r['assert']:
        result = AGIObject(cid_of['dcr::assert'],
                           {cid_of['dc::assert_expression']: pack_expr(line[1])})
    elif head == r['for']:
        result = AGIObject(cid_of['dcr::for'],
                           {cid_of['dc::iterator_index']: line[1],
                            cid_of['dc::end_value']: pack_expr(line[2]),
                            cid_of['dc::for_block']: pack_sub_block(line[3])})
    elif head == r['while']:
        result = AGIObject(cid_of['dcr::while'],
                           {cid_of['dc::expression_for_judging']: pack_expr(line[1]),
                            cid_of['dc::while_block']: pack_sub_block(line[2])})
    elif head == r['break']:
        result = AGIObject(cid_of['dcr::break'])
    elif head == r['if']:
        result = AGIObject(cid_of['dcr::if'],
                           {cid_of['dc::expression_for_judging']: pack_expr(line[1]),
                            cid_of['dc::if_block']: pack_sub_block(line[2]),
                            cid_of['dc::elif_modules']: pack_list(line[3], 'elif'),
                            cid_of['dc::else_block']: pack_sub_block(line[4])})
    elif head == r['append']:
        result = AGIObject(cid_of['dcr::append'],
                           {cid_of['dc::target_list']: pack_expr(line[1]),
                            cid_of['dc::element']: pack_expr(line[2])})
    elif head == r['remove']:
        result = AGIObject(cid_of['dcr::remove'],
                           {cid_of['dc::target_list']: pack_expr(line[1]),
                            cid_of['dc::expression_for_constraint']: pack_expr(line[2])})
    elif head == r['request']:
        result = AGIObject(cid_of['dcr::request'],
                           {cid_of['dc::requested_registers']: pack_list(line[1], 'number'),
                            cid_of['dc::expression_for_constraint']: pack_expr(line[2]),
                            cid_of['dc::provided_block']: pack_sub_block(line[3])})
    elif head == r['call_none_return_func']:
        result = AGIObject(cid_of['dcr::call_none_return_func'],
                           {cid_of['dc::function_name']: line[1],
                            cid_of['dcr::function_params']: pack_list(line[2], 'expr')})
    else:
        raise AGIException('Unexpected head.')
    return result


def code_to_object(code: list) -> AGIObject:
    lines = list()
    for line in code:
        line_obj = pack_line(line)
        lines.append(line_obj)
    result = AGIObject(cid_of['dynamic_code'], {cid_of['dc::lines']: AGIList(lines)})

    return result
