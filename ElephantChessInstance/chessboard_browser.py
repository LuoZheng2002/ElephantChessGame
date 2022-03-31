from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeDriver.code_driver import get_agi_list
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException


def print_chessboard(xq_chessboard: AGIObject):
    chessboard = [[None for i in range(9)] for i in range(10)]
    for i in xq_chessboard.attributes[cid_of['xq::pieces']].get_list():
        name = cid_reverse[i.attributes[cid_of['xq::piece_name']].concept_id][4:]
        if i.attributes[cid_of['xq::piece_owner']].concept_id == cid_of['xq::red_team']:
            name = name.upper()
        else:
            name = name.lower()
        position = [None, None]
        position[0] = to_integer(get_agi_list(i.attributes[cid_of['xq::position']]).get_element(0))
        position[1] = to_integer(get_agi_list(i.attributes[cid_of['xq::position']]).get_element(1))
        chessboard[position[1]][position[0]] = name
    print('#################################################################################')
    print('####### 0 ##### 1 ##### 2 ##### 3 ##### 4 ##### 5 ##### 6 ##### 7 ##### 8 #######')

    for k, j in enumerate(chessboard):
        print(str(k).rjust(4, '#') + ' ', end='')
        for i in j:
            if i is None:
                print('[     ] ', end='')
            else:
                if len(i) <= 3:
                    i = ' ' + i
                print('[' + i.ljust(5, ' ') + '] ', end='')
        print('####')
    print('#################################################################################')
