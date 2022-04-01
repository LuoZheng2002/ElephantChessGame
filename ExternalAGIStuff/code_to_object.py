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
    head = expr[0]
    if head == r['input'] or r['iterator']:
        params = [expr[1]]
    elif head == r['reg']:
        params = [expr[1], pack_list(expr[2], 'expr')]
    elif head == r['call']:
        params = [AGIObject(expr[1]), pack_list(expr[2], 'expr')]
    elif head == r['concept_instance']:
        params = []
    result = AGIObject(cid_of['dc::expression'], {cid_of['dc::head']: head,
                                                  cid_of['dc::params']: AGIList(params)})


def pack_sub_block(sub_block: list) -> AGIObject:
    pass


def pack_list(list_param: list, list_type) -> AGIList:
    pass


def code_to_object(code: list) -> AGIObject:
    lines = list()
    for line in code:
        head = line[0]
        if head == r['assign'] or r['assign_as_reference'] or r['append'] or r['remove']:
            params = [pack_expr(line[1]), pack_expr(line[2])]
        elif head == r['return'] or r['assert']:
            params = [pack_expr(line[1])]
        elif head == r['for']:
            params = [line[1], pack_expr(line[2]), pack_sub_block(line[3])]
        elif head == r['while']:
            params = [pack_expr(line[1]), pack_sub_block(line[2])]
        elif head == r['break']:
            params = list()
        elif head == r['if']:
            params = [pack_expr(line[1]), pack_sub_block(line[2]), pack_list(line[3], 'elif'), pack_sub_block(line[4])]
        elif head == r['request']:
            params = [pack_list(line[1], 'expr'), pack_expr(line[2]), pack_sub_block(line[3])]
        else:
            raise AGIException('Unexpected head at the beginning of a line.')
        line_obj = AGIObject(cid_of['dc::line'], {cid_of['dc::head']: head,
                                                  cid_of['dc::params']: AGIList(params)})
        lines.append(line_obj)
    result = AGIObject(cid_of['dynamic_code'], {cid_of['dc::lines']: AGIList(lines)})

    return result
